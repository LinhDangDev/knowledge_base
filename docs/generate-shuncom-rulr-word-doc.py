from __future__ import annotations

import json
import shutil
import struct
import subprocess
import tempfile
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


DOCS_DIR = Path("D:/OneDrive - linhdangdev/Documents/Obsidian Vault/ShucomAIOT/docs")
OUTPUTS = {
    "vi": DOCS_DIR / "shuncom-rulr-system-workflows-and-api-endpoints-vi.docx",
    "en": DOCS_DIR / "shuncom-rulr-system-workflows-and-api-endpoints-en.docx",
}

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
EMU_PER_PIXEL = 9525
MAX_IMAGE_WIDTH_EMU = 5_850_000


@dataclass(frozen=True)
class DeviceEntry:
    name: str
    purpose_vi: str
    purpose_en: str
    deployment_vi: str
    deployment_en: str
    configuration_vi: str
    configuration_en: str
    operations_vi: str
    operations_en: str


@dataclass(frozen=True)
class WorkflowEntry:
    title_vi: str
    title_en: str
    objective_vi: str
    objective_en: str
    steps_vi: tuple[str, ...]
    steps_en: tuple[str, ...]
    apis: tuple[str, ...]


@dataclass(frozen=True)
class ApiGroup:
    title_vi: str
    title_en: str
    items: tuple[tuple[str, str, str], ...]


@dataclass(frozen=True)
class DiagramSpec:
    key: str
    title_vi: str
    title_en: str
    caption_vi: str
    caption_en: str
    mermaid_vi: str
    mermaid_en: str


DEVICES = (
    DeviceEntry(
        name="Gateway",
        purpose_vi="Thiết bị trung tâm kết nối và quản lý các thiết bị con trong cùng hệ thống triển khai.",
        purpose_en="Central communication hub used to connect and manage subordinate field devices.",
        deployment_vi="Thường được triển khai ở lớp hạ tầng hiện trường, làm đầu mối kết nối cho controller, meter và các điểm thu thập liên quan.",
        deployment_en="Typically deployed at the field infrastructure layer to anchor controllers, meters, and related collection points.",
        configuration_vi="Biểu mẫu cấu hình hỗ trợ product name, device number, project, group, tọa độ, altitude và các association như distribution box, circuit control, electricity meter khi áp dụng.",
        configuration_en="The configuration form supports product name, device number, project, group, coordinates, altitude, and associations such as distribution box, circuit control, and electricity meter when applicable.",
        operations_vi="Hỗ trợ các tác vụ vận hành như synchronization, configure circuits, screen password, three-phase ratio và clear local rules nếu thiết bị hỗ trợ.",
        operations_en="Operational actions include synchronization, circuit configuration, screen password setup, three-phase ratio settings, and clearing local rules when supported.",
    ),
    DeviceEntry(
        name="Industrial Controller",
        purpose_vi="Thiết bị điều khiển công nghiệp dùng cho các kịch bản điều khiển chuyên biệt trong hệ sinh thái hiện có.",
        purpose_en="Industrial control endpoint used for specialized control scenarios within the currently supported ecosystem.",
        deployment_vi="Được dùng trong các triển khai yêu cầu tích hợp điểm điều khiển công nghiệp theo product model cụ thể.",
        deployment_en="Used in deployments that require integration with industrial control points tied to a specific product model.",
        configuration_vi="Tập trường cấu hình phụ thuộc product/subtype thực tế và cần bám theo model thiết bị đã được chọn.",
        configuration_en="Its field set depends on the selected product or subtype and should follow the actual device model.",
        operations_vi="Hành vi vận hành được định hướng bởi model thiết bị; tài liệu hiện tại mô tả ở mức supported type thay vì luồng chi tiết riêng.",
        operations_en="Operational behavior is model-driven; current documentation describes it as a supported type rather than a dedicated detailed flow.",
    ),
    DeviceEntry(
        name="Smart Light Controller",
        purpose_vi="Thiết bị điều khiển chiếu sáng, phục vụ bật/tắt, dimming và các kịch bản điều khiển đèn theo nhiều giao thức truyền thông.",
        purpose_en="Lighting control device used for switching, dimming, and smart lighting operations across multiple communication patterns.",
        deployment_vi="Được dùng trong các dự án chiếu sáng thông minh, có thể hoạt động theo dạng pass-through, direct communication hoặc LoRa tùy subtype.",
        deployment_en="Used in smart lighting projects and can operate in pass-through, direct communication, or LoRa modes depending on subtype.",
        configuration_vi="Trường cấu hình thay đổi theo subtype; một số subtype yêu cầu gateway, một số yêu cầu associated luminaires và có thể cần light pole, project, group, vị trí.",
        configuration_en="Configuration fields change by subtype; some subtypes require a gateway, some require associated luminaires, and some may also need light pole, project, group, and location context.",
        operations_vi="Các action thường thấy gồm clear, timing calibration, local rule enable, read data, device synchronization và GPS switch khi loại controller hỗ trợ.",
        operations_en="Common supported actions include clear, timing calibration, local rule enablement, data reading, device synchronization, and GPS switching when supported by the controller type.",
    ),
    DeviceEntry(
        name="Power Distribution Control (PDC)",
        purpose_vi="Thiết bị quản lý và điều phối phân phối điện ở cấp tủ điện hoặc điểm điều khiển nguồn.",
        purpose_en="Device used to manage and coordinate power distribution at cabinet or power control level.",
        deployment_vi="Phù hợp với các dự án cần quản lý hạ tầng nguồn và liên kết với thiết bị điều khiển hoặc đo đếm liên quan.",
        deployment_en="Suitable for deployments that require managed power infrastructure with links to control and metering devices.",
        configuration_vi="Thường liên kết với gateway, circuit hoặc meter; cấu hình cụ thể phụ thuộc kiến trúc thiết bị được chọn trong dự án.",
        configuration_en="Often linked with gateways, circuits, or meters, with exact configuration depending on the chosen deployment architecture.",
        operations_vi="Được xem như thành phần hạ tầng nguồn trong hệ thống; tài liệu hiện tại mô tả rõ vai trò và quan hệ hơn là luồng riêng chi tiết.",
        operations_en="Documented primarily as a power infrastructure component, with emphasis on role and associations rather than a separate detailed workflow.",
    ),
    DeviceEntry(
        name="Weather Sensor",
        purpose_vi="Nguồn dữ liệu thời tiết phục vụ hiển thị, giám sát và các kịch bản rule hoặc dashboard liên quan đến môi trường.",
        purpose_en="Weather telemetry source used for monitoring, dashboard presentation, and environment-related rule scenarios.",
        deployment_vi="Được dùng khi dự án cần bổ sung dữ liệu thời tiết vào giám sát vận hành hoặc điều kiện kích hoạt rule.",
        deployment_en="Used when a project needs weather data as part of operational monitoring or rule triggering context.",
        configuration_vi="Cấu hình phụ thuộc model cảm biến và nhu cầu telemetry; có thể chịu ảnh hưởng bởi project, group và vị trí lắp đặt.",
        configuration_en="Configuration depends on the sensor model and telemetry requirements and may depend on project, group, and installation location.",
        operations_vi="Vai trò chính là cung cấp telemetry môi trường; tài liệu hiện tại mô tả ở mức supported device type.",
        operations_en="Its primary role is environmental telemetry delivery; current documentation covers it at supported device type level.",
    ),
    DeviceEntry(
        name="Environmental Sensor",
        purpose_vi="Thiết bị cảm biến môi trường dùng để ghi nhận dữ liệu hiện trường phục vụ giám sát và phân tích.",
        purpose_en="Environmental sensing device used to capture field data for monitoring and analysis.",
        deployment_vi="Phù hợp với các bài toán cần đo đạc điều kiện môi trường tại dự án hoặc khu vực vận hành cụ thể.",
        deployment_en="Suitable for use cases that require environmental measurements within a project or operational area.",
        configuration_vi="Dữ liệu cấu hình bám theo model cảm biến và loại telemetry cần theo dõi; project, group và location vẫn là ngữ cảnh quan trọng.",
        configuration_en="Configuration follows the selected sensor model and telemetry scope, while project, group, and location remain important operating context.",
        operations_vi="Được dùng như nguồn dữ liệu cho dashboard, analytics hoặc rule conditions tùy nghiệp vụ.",
        operations_en="Used as a data source for dashboards, analytics, or rule conditions depending on the business scenario.",
    ),
    DeviceEntry(
        name="Smart Electric Meter",
        purpose_vi="Thiết bị đo điện năng, phục vụ thống kê tiêu thụ điện và hiển thị energy analytics trong dự án.",
        purpose_en="Energy metering device used to capture power consumption data and feed project-level energy analytics.",
        deployment_vi="Thường xuất hiện trong các dự án cần theo dõi điện năng, KPI tiêu thụ và hiển thị số liệu năng lượng trên dashboard.",
        deployment_en="Typically used in deployments that require energy tracking, consumption KPIs, and dashboard-based reporting.",
        configuration_vi="Biểu mẫu thường hỗ trợ associated gateway, meter-related fields, project, group và location; một số trường kỹ thuật phụ thuộc model meter.",
        configuration_en="The form typically supports an associated gateway, meter-related fields, project, group, and location; some technical fields depend on the meter model.",
        operations_vi="Dữ liệu của meter là nguồn đầu vào quan trọng cho energy overview, reporting và các phân tích vận hành liên quan đến điện năng.",
        operations_en="Meter data acts as a key source for energy overview screens, reporting, and operations-related energy analysis.",
    ),
    DeviceEntry(
        name="Lighting Pole",
        purpose_vi="Thực thể hạ tầng vật lý dùng để gắn kết thiết bị với cột đèn hoặc điểm lắp đặt ngoài hiện trường.",
        purpose_en="Physical infrastructure record used to anchor devices to a lighting pole or real-world installation point.",
        deployment_vi="Hữu ích trong các dự án cần ánh xạ thiết bị với hạ tầng thực, phục vụ tổ chức tài sản và vị trí ngoài hiện trường.",
        deployment_en="Useful in deployments that need to map devices to real field infrastructure for asset organization and location context.",
        configuration_vi="Biểu mẫu thường bám theo các trường thiết bị chuẩn, đồng thời hỗ trợ project và group để giữ đúng ngữ cảnh vận hành.",
        configuration_en="The form follows common device fields and supports project and group assignments to preserve operational context.",
        operations_vi="Đóng vai trò container hạ tầng và điểm neo cho các thiết bị liên quan trong cùng khu vực triển khai.",
        operations_en="Acts as an infrastructure container and anchor point for related devices within the same deployment area.",
    ),
    DeviceEntry(
        name="Lighting Fixture",
        purpose_vi="Tài sản đèn hoặc bộ đèn dùng trong các kịch bản điều khiển chiếu sáng, đặc biệt khi controller cần association tới tải đèn cụ thể.",
        purpose_en="Lighting asset used in smart lighting scenarios, especially where a controller must be associated with a specific lighting load.",
        deployment_vi="Được dùng trong các triển khai chiếu sáng nơi controller và bộ đèn cần được liên kết rõ ràng để phục vụ điều khiển và hiển thị.",
        deployment_en="Used in lighting deployments where controllers and luminaires must be explicitly linked for control and presentation purposes.",
        configuration_vi="Một số luồng controller yêu cầu associated luminaires; thiếu association phù hợp có thể làm controller không điều khiển đúng đối tượng.",
        configuration_en="Some controller flows require associated luminaires; without the correct association, the controller may not target the intended lighting asset.",
        operations_vi="Là thành phần quan trọng trong mô hình lighting asset, hỗ trợ điều khiển chính xác và giữ tính toàn vẹn của quan hệ controller-fixture.",
        operations_en="It is a critical part of the lighting asset model, supporting precise control and maintaining controller-to-fixture integrity.",
    ),
    DeviceEntry(
        name="Smart Water Meter",
        purpose_vi="Thiết bị đo nước thông minh trong tập supported device hiện tại của nền tảng.",
        purpose_en="Smart water metering device included in the platform's currently supported device set.",
        deployment_vi="Phù hợp với các bài toán mở rộng từ đo điện sang đo nước trong cùng môi trường quản lý tài sản và telemetry.",
        deployment_en="Suitable for deployments that extend from electrical metering into water metering within the same telemetry and asset management environment.",
        configuration_vi="Tài liệu hiện tại mô tả ở mức supported type; schema và association chi tiết cần bám theo model thực tế khi triển khai.",
        configuration_en="Current documentation describes it at supported type level; detailed schema and associations should follow the actual deployed model.",
        operations_vi="Vai trò chính là cung cấp dữ liệu đo đếm trong cùng nền tảng quan sát và vận hành.",
        operations_en="Its primary role is to provide metering data within the same monitoring and operations platform.",
    ),
    DeviceEntry(
        name="Leakage Monitoring",
        purpose_vi="Thiết bị giám sát rò rỉ phục vụ các tình huống cảnh báo và an toàn ngoài hiện trường.",
        purpose_en="Leakage monitoring device used for alarm-oriented and safety-oriented field scenarios.",
        deployment_vi="Được triển khai khi dự án cần phát hiện bất thường liên quan đến rò rỉ và phản ứng sớm qua alarm handling.",
        deployment_en="Deployed where the project needs early detection of leakage-related abnormalities and alarm-based response.",
        configuration_vi="Cấu hình chi tiết phụ thuộc model cảm biến và ngưỡng nghiệp vụ; thường gắn với logic cảnh báo và telemetry tại project.",
        configuration_en="Detailed configuration depends on the sensor model and business thresholds and is usually tied to project-level telemetry and alarm logic.",
        operations_vi="Thiết bị này phù hợp với các use case safety monitoring và tạo dữ liệu đầu vào cho cảnh báo.",
        operations_en="This device is suited for safety monitoring use cases and supplies input signals for alarm generation.",
    ),
    DeviceEntry(
        name="Indoor Light Controller",
        purpose_vi="Thiết bị điều khiển chiếu sáng trong nhà, được giữ như một loại thiết bị hỗ trợ riêng trong tài liệu hiện tại.",
        purpose_en="Indoor lighting control device maintained as an explicit supported device type in the current documentation set.",
        deployment_vi="Phù hợp với các không gian trong nhà cần điều khiển chiếu sáng theo ngữ cảnh dự án và vận hành tập trung.",
        deployment_en="Suitable for indoor spaces that require lighting control within the same centralized project operations model.",
        configuration_vi="Có thể có subtype riêng; cấu hình cụ thể nên bám theo model sản phẩm được sử dụng trong triển khai thực tế.",
        configuration_en="It may have its own subtype patterns; exact configuration should follow the deployed product model.",
        operations_vi="Vai trò vận hành tập trung vào điều khiển chiếu sáng indoor và liên kết với context dashboard hoặc nhóm vận hành khi cần.",
        operations_en="Its operational role centers on indoor lighting control and linkage to dashboard or group-based operating context when needed.",
    ),
    DeviceEntry(
        name="Scene Panel",
        purpose_vi="Thiết bị điều khiển theo ngữ cảnh hoặc scene, hỗ trợ thao tác tương tác trong tập thiết bị hiện có.",
        purpose_en="Scene-based interaction device that supports contextual control within the current device ecosystem.",
        deployment_vi="Được dùng khi cần kích hoạt nhanh các kịch bản vận hành hoặc điều khiển nhóm thiết bị theo trải nghiệm người dùng.",
        deployment_en="Used where rapid scene activation or user-facing interaction is required for grouped operational control.",
        configuration_vi="Tài liệu hiện tại mô tả như supported type ở mức khái quát; cấu hình chi tiết phụ thuộc model panel thực tế.",
        configuration_en="Current documentation describes it as a supported type at high level; detailed configuration depends on the actual panel model.",
        operations_vi="Vai trò chính là hỗ trợ thao tác scene hoặc interaction flow trong bối cảnh vận hành dự án.",
        operations_en="Its main role is to support scene-based or interaction-driven operational flows within a project.",
    ),
    DeviceEntry(
        name="Accessory Device",
        purpose_vi="Thiết bị phụ trợ dùng để hoàn thiện hệ sinh thái thiết bị trong cùng nền tảng quản lý.",
        purpose_en="Supporting accessory device used to complete the device ecosystem within the same management platform.",
        deployment_vi="Phù hợp với các tình huống cần bổ sung thành phần phụ trợ cho asset landscape của dự án.",
        deployment_en="Suitable for deployments that require accessory components as part of the overall project asset landscape.",
        configuration_vi="Tài liệu hiện tại chuẩn hóa tên gọi nhưng chưa đi sâu vào luồng riêng; cấu hình cần theo model accessory cụ thể.",
        configuration_en="Current documentation normalizes the naming but does not provide a dedicated flow; configuration should follow the specific accessory model.",
        operations_vi="Được xem như loại thiết bị hỗ trợ, có vai trò bổ sung cho kịch bản triển khai tổng thể.",
        operations_en="Treated as a supporting device type with a complementary role in the overall deployment scenario.",
    ),
)


WORKFLOWS = (
    WorkflowEntry(
        title_vi="Đăng nhập và khởi tạo phiên làm việc",
        title_en="Sign-in and session initialization",
        objective_vi="Xác thực người dùng và nạp role, permission, management scope trước khi vào hệ thống.",
        objective_en="Authenticate the user and load roles, permissions, and management scope before entering the platform.",
        steps_vi=(
            "Người dùng mở trang đăng nhập và nhập thông tin xác thực.",
            "Hệ thống xác thực tài khoản và kiểm tra trạng thái active của người dùng.",
            "Sau khi đăng nhập thành công, hệ thống tải thông tin người dùng, quyền và phạm vi quản lý.",
            "Dashboard và menu điều hướng được dựng theo đúng quyền và scope của tài khoản.",
        ),
        steps_en=(
            "The user opens the login page and submits valid credentials.",
            "The platform authenticates the account and checks that the user is active.",
            "After successful sign-in, the system loads the user profile, permissions, and management scope.",
            "The dashboard and navigation are then rendered according to the approved access scope.",
        ),
        apis=("POST /auth/login", "POST /auth/refresh", "GET /auth/me", "POST /auth/logout"),
    ),
    WorkflowEntry(
        title_vi="Tạo user, role và management scope",
        title_en="Create users, roles, and management scope",
        objective_vi="Thiết lập ai được nhìn thấy dữ liệu nào và thao tác được trên phạm vi project, group và product category nào.",
        objective_en="Define who can see which data and which project, group, and product-category scope each user can operate within.",
        steps_vi=(
            "Quản trị viên tạo user mới hoặc cập nhật user hiện có.",
            "Quản trị viên tạo hoặc gán role theo chức năng nghiệp vụ.",
            "Permissions và management scope được áp vào user hoặc role đích.",
            "Từ thời điểm đó, dashboard, danh sách thiết bị và các tác vụ vận hành được giới hạn theo scope đã lưu.",
        ),
        steps_en=(
            "An administrator creates a new user or updates an existing one.",
            "Roles are created or assigned based on business responsibilities.",
            "Permissions and management scope are applied to the target user or role.",
            "From that point onward, dashboards, device lists, and operations are filtered by the saved scope.",
        ),
        apis=(
            "POST /users",
            "PUT /users/{id}/roles",
            "PUT /users/{id}/scope",
            "POST /roles",
            "GET /roles/permissions",
        ),
    ),
    WorkflowEntry(
        title_vi="Tạo project và phân cấp sub-project",
        title_en="Create projects and sub-project hierarchy",
        objective_vi="Thiết lập ngữ cảnh tổ chức chính cho dashboard, GIS, rules, analytics và phạm vi hiển thị thiết bị.",
        objective_en="Establish the primary operating context for dashboards, GIS, rules, analytics, and device visibility.",
        steps_vi=(
            "Người dùng tạo project mới từ cây project với tên, manager, địa chỉ và tọa độ.",
            "Project gốc hoặc sub-project được lưu vào cây phân cấp của hệ thống.",
            "Sub-project trở thành phạm vi vận hành chính cho phân bổ thiết bị, dashboard và GIS.",
            "Các cấu hình hiển thị, lịch vận hành và kế hoạch tiêu thụ điện có thể gắn theo project đó.",
        ),
        steps_en=(
            "The user creates a new project from the project tree with name, manager, address, and coordinates.",
            "The root project or sub-project is stored in the platform hierarchy.",
            "The sub-project becomes the primary operating scope for device distribution, dashboards, and GIS.",
            "Display settings, operating schedules, and power consumption plans can then be assigned to that project.",
        ),
        apis=("GET /projects", "POST /projects", "GET /projects/tree", "GET /projects/{id}/children"),
    ),
    WorkflowEntry(
        title_vi="Gán thiết bị vào project và group",
        title_en="Associate devices with projects and groups",
        objective_vi="Đưa thiết bị vào đúng ngữ cảnh quản lý để phục vụ dashboard, rules, GIS và vận hành tập trung.",
        objective_en="Place devices into the correct operating context for dashboards, rules, GIS, and centralized operations.",
        steps_vi=(
            "Người dùng chọn project hoặc group đích trong phần cấu hình thiết bị.",
            "Thiết bị được tìm kiếm, chọn và xác nhận liên kết.",
            "Hệ thống lưu association ở cấp project hoặc group.",
            "Ngay sau đó, thiết bị xuất hiện trong đúng ngữ cảnh dashboard, analytics và operation control.",
        ),
        steps_en=(
            "The user selects the target project or group inside device management.",
            "The device is searched, selected, and confirmed for association.",
            "The platform stores the project-level or group-level association.",
            "The device then appears in the correct dashboard, analytics, and operation-control context.",
        ),
        apis=(
            "GET /projects/{id}/devices",
            "POST /device-groups/{id}/devices",
            "DELETE /device-groups/{id}/devices",
            "PATCH /devices/{id}",
        ),
    ),
    WorkflowEntry(
        title_vi="Onboard thiết bị theo loại",
        title_en="Onboard devices by type",
        objective_vi="Tạo bản ghi thiết bị với biểu mẫu động theo category, product và subtype.",
        objective_en="Create device records through dynamic forms driven by category, product, and subtype.",
        steps_vi=(
            "Người dùng chọn Type view và chọn loại thiết bị cần tạo.",
            "Biểu mẫu hiển thị các trường Device Information, Product Information và Asset Info theo model tương ứng.",
            "Người dùng nhập project, group, vị trí và các trường kỹ thuật bắt buộc.",
            "Hệ thống validate dữ liệu theo loại thiết bị trước khi lưu vào danh sách quản lý.",
        ),
        steps_en=(
            "The user opens the Type view and selects the device type to create.",
            "The form presents Device Information, Product Information, and Asset Info based on the selected model.",
            "The user enters project, group, location, and required technical fields.",
            "The platform validates the data by device type before storing the new record.",
        ),
        apis=("GET /device-types", "GET /device-types/{code}", "POST /devices", "PUT /devices/{id}"),
    ),
    WorkflowEntry(
        title_vi="Cấu hình dashboard theo project",
        title_en="Configure project-level dashboard presentation",
        objective_vi="Thiết lập display information, lighting schedules và electricity consumption plan cho từng project.",
        objective_en="Configure display information, lighting schedules, and the electricity consumption plan for each project.",
        steps_vi=(
            "Người dùng mở project và đi vào phần Display Information.",
            "Style, title, module hiển thị và usage scenario được cấu hình theo nhu cầu dự án.",
            "Lighting schedules today và electricity consumption plan được thiết lập theo cùng ngữ cảnh project.",
            "Homepage dashboard cập nhật để phản ánh đúng cấu hình đã lưu.",
        ),
        steps_en=(
            "The user opens a project and enters the Display Information area.",
            "Styles, titles, visible modules, and usage scenario are configured for the project.",
            "Lighting schedules and the electricity consumption plan are then set within the same project context.",
            "The homepage dashboard updates to reflect the saved presentation settings.",
        ),
        apis=(
            "GET /projects/{id}",
            "PUT /projects/{id}",
            "GET /dashboard/statistics",
            "GET /dashboard/map-data",
        ),
    ),
    WorkflowEntry(
        title_vi="Phân bố GIS và quản lý bản đồ",
        title_en="GIS distribution and map-based management",
        objective_vi="Đưa thiết bị lên bản đồ dự án để hỗ trợ hiển thị, định vị và điều hành ngoài hiện trường.",
        objective_en="Place devices onto the project map to support visualization, location management, and field operations.",
        steps_vi=(
            "Người dùng chọn project có ngữ cảnh GIS phù hợp.",
            "Thiết bị có tọa độ được chọn để đặt đơn lẻ hoặc phân bổ hàng loạt trên tuyến.",
            "Người dùng tinh chỉnh vị trí khi cần để phản ánh đúng hiện trạng ngoài hiện trường.",
            "Dashboard map và operation control sau đó sử dụng chính dữ liệu vị trí này.",
        ),
        steps_en=(
            "The user selects a project with the appropriate GIS context.",
            "Devices with coordinates are placed individually or distributed along a route in batch.",
            "Locations can be fine-tuned to reflect the real field condition.",
            "The dashboard map and operation control then consume this location dataset.",
        ),
        apis=("GET /projects/{id}", "GET /dashboard/map-data", "PATCH /devices/{id}", "PUT /devices/{id}"),
    ),
    WorkflowEntry(
        title_vi="Tạo platform rules",
        title_en="Create platform rules",
        objective_vi="Thiết lập automation tập trung ở tầng platform cho các điều kiện kích hoạt và hành động vận hành.",
        objective_en="Configure centralized platform-side automation for trigger conditions and operational actions.",
        steps_vi=(
            "Người dùng tạo platform rule với metadata, effective period và remarks.",
            "Điều kiện kích hoạt và hành động thực thi được cấu hình theo loại bài toán.",
            "Target device, group hoặc category được chọn theo phạm vi nghiệp vụ.",
            "Rule có thể được enable, disable hoặc chạy thử bằng hành động thực thi phù hợp.",
        ),
        steps_en=(
            "The user creates a platform rule with metadata, effective period, and remarks.",
            "Trigger conditions and execution actions are configured for the required use case.",
            "Target devices, groups, or categories are selected according to business scope.",
            "The rule can then be enabled, disabled, or manually executed where supported.",
        ),
        apis=(
            "GET /rules/platform",
            "POST /rules/platform",
            "POST /rules/platform/{id}/enable",
            "POST /rules/platform/{id}/execute",
        ),
    ),
    WorkflowEntry(
        title_vi="Tạo local rules và đồng bộ xuống thiết bị",
        title_en="Create local rules and synchronize them to devices",
        objective_vi="Đưa automation đơn giản xuống gateway hoặc thiết bị để giảm phụ thuộc vào kết nối mạng thời gian thực.",
        objective_en="Push lightweight automation down to gateways or devices to reduce dependency on real-time network connectivity.",
        steps_vi=(
            "Người dùng tạo local rule với trigger và action phù hợp theo loại thiết bị.",
            "Rule được lưu ở tầng platform như một cấu hình cần đồng bộ.",
            "Người dùng gửi lệnh sync xuống gateway hoặc thiết bị đích.",
            "Kết quả sync được trả về theo từng thiết bị để phục vụ xác nhận và troubleshooting.",
        ),
        steps_en=(
            "The user creates a local rule with the required trigger and action pattern for the target device type.",
            "The rule is stored on the platform as a configuration awaiting synchronization.",
            "A sync command is sent to the target gateway or device.",
            "Per-device synchronization results are returned for validation and troubleshooting.",
        ),
        apis=("GET /rules/local", "POST /rules/local", "POST /rules/local/{id}/sync", "DELETE /rules/local/gateway/{gatewayId}"),
    ),
    WorkflowEntry(
        title_vi="Tạo alarm rules và xử lý cảnh báo",
        title_en="Create alarm rules and handle alerts",
        objective_vi="Phát hiện bất thường, gửi cảnh báo và hỗ trợ đội vận hành xử lý theo severity và trạng thái xử lý.",
        objective_en="Detect abnormal conditions, send alerts, and support operations teams in handling them by severity and processing status.",
        steps_vi=(
            "Người dùng tạo receiving group và alarm rule theo điều kiện mong muốn.",
            "Hệ thống theo dõi dữ liệu và sự kiện để tạo alarm khi điều kiện được thỏa mãn.",
            "Alarm được hiển thị trong operation & maintenance để operator theo dõi.",
            "Operator có thể acknowledge, resolve hoặc xử lý hàng loạt tùy theo quy trình vận hành.",
        ),
        steps_en=(
            "The user creates a receiving group and an alarm rule for the required condition set.",
            "The platform monitors data and events and generates alarms when conditions are met.",
            "Alarms appear in the operations and maintenance area for operator review.",
            "Operators can acknowledge, resolve, or process alarms in batch according to the operating procedure.",
        ),
        apis=("POST /rules/alarm", "GET /alarms", "POST /alarms/{id}/acknowledge", "POST /alarms/{id}/resolve"),
    ),
    WorkflowEntry(
        title_vi="Operation control, device detail và analytics",
        title_en="Operation control, device detail, and analytics",
        objective_vi="Cho phép vận hành tức thời, theo dõi trạng thái thiết bị và phân tích dữ liệu lịch sử trong cùng một bối cảnh dự án.",
        objective_en="Enable immediate operations, device-level status review, and historical analysis within the same project context.",
        steps_vi=(
            "Người dùng vào operation control qua map hoặc device list.",
            "Thiết bị hoặc nhóm thiết bị được chọn để thực thi quick actions phù hợp.",
            "Device detail hiển thị overview, alarm information, operation records, rules và dữ liệu lịch sử.",
            "Statistical analysis và reporting được dùng để xem xu hướng, KPI và xuất dữ liệu khi cần.",
        ),
        steps_en=(
            "The user enters operation control through the map view or device list.",
            "A device or group of devices is selected for the required quick action.",
            "The device detail page presents overview data, alarms, operation records, rules, and historical information.",
            "Statistical analysis and reporting are then used to review trends, KPIs, and exports when required.",
        ),
        apis=(
            "POST /devices/{id}/actions/power-on",
            "POST /devices/{id}/actions/dim",
            "GET /devices/{id}/metrics/history",
            "GET /reports/operations",
        ),
    ),
)


API_GROUPS = (
    ApiGroup(
        title_vi="Authentication APIs",
        title_en="Authentication APIs",
        items=(
            ("POST /auth/login", "Đăng nhập và khởi tạo phiên người dùng.", "Authenticate the user and create a session."),
            ("POST /auth/refresh", "Gia hạn access token.", "Refresh an access token."),
            ("POST /auth/logout", "Kết thúc phiên hiện tại.", "Terminate the current session."),
            ("GET /auth/me", "Lấy hồ sơ người dùng hiện tại.", "Get the current user profile."),
            ("POST /auth/password/change", "Đổi mật khẩu người dùng.", "Change the user password."),
            ("POST /auth/password/reset-request", "Tạo yêu cầu đặt lại mật khẩu.", "Request a password reset."),
            ("POST /auth/password/reset", "Đặt lại mật khẩu bằng token.", "Reset the password by token."),
            ("POST /auth/mfa/enable", "Bật xác thực đa yếu tố.", "Enable multi-factor authentication."),
            ("POST /auth/mfa/disable", "Tắt xác thực đa yếu tố.", "Disable multi-factor authentication."),
            ("POST /auth/mfa/verify", "Xác thực mã MFA.", "Verify an MFA code."),
        ),
    ),
    ApiGroup(
        title_vi="User, organization, and role APIs",
        title_en="User, organization, and role APIs",
        items=(
            ("GET /users", "Liệt kê và lọc user.", "List and filter users."),
            ("POST /users", "Tạo user mới.", "Create a new user."),
            ("PUT /users/{id}", "Cập nhật hồ sơ user.", "Update a user profile."),
            ("PATCH /users/{id}/status", "Bật hoặc vô hiệu hóa user.", "Enable or disable a user."),
            ("PUT /users/{id}/roles", "Gán role cho user.", "Assign roles to a user."),
            ("PUT /users/{id}/scope", "Cập nhật management scope.", "Update management scope."),
            ("GET /organizations", "Liệt kê tổ chức.", "List organizations."),
            ("POST /organizations", "Tạo tổ chức.", "Create an organization."),
            ("GET /organizations/{id}/projects", "Liệt kê project thuộc tổ chức.", "List projects under an organization."),
            ("GET /roles", "Liệt kê role.", "List roles."),
            ("POST /roles", "Tạo role mới.", "Create a new role."),
            ("GET /roles/permissions", "Liệt kê permission khả dụng.", "List available permissions."),
        ),
    ),
    ApiGroup(
        title_vi="Project APIs",
        title_en="Project APIs",
        items=(
            ("GET /projects", "Liệt kê project hierarchy.", "List the project hierarchy."),
            ("GET /projects/{id}", "Lấy thông tin chi tiết project.", "Get project details."),
            ("POST /projects", "Tạo project.", "Create a project."),
            ("PUT /projects/{id}", "Cập nhật project và cấu hình liên quan.", "Update a project and related settings."),
            ("DELETE /projects/{id}", "Xóa project theo rule nghiệp vụ hiện hành.", "Delete a project subject to business rules."),
            ("GET /projects/{id}/devices", "Liệt kê thiết bị theo project.", "List devices under a project."),
            ("GET /projects/{id}/children", "Liệt kê sub-project.", "List child projects."),
            ("GET /projects/tree", "Lấy cấu trúc cây project hoàn chỉnh.", "Get the full project tree."),
        ),
    ),
    ApiGroup(
        title_vi="Device APIs",
        title_en="Device APIs",
        items=(
            ("GET /devices", "Liệt kê và lọc thiết bị.", "List and filter devices."),
            ("GET /devices/{id}", "Lấy thông tin chi tiết thiết bị.", "Get device details."),
            ("POST /devices", "Tạo bản ghi thiết bị mới.", "Create a new device record."),
            ("PUT /devices/{id}", "Cập nhật cấu hình đầy đủ của thiết bị.", "Update a device configuration fully."),
            ("PATCH /devices/{id}", "Cập nhật một phần dữ liệu thiết bị.", "Partially update a device."),
            ("DELETE /devices/{id}", "Thực hiện luồng recycle hoặc delete theo chính sách hệ thống.", "Execute recycle or delete behavior according to platform policy."),
            ("GET /device-types", "Liệt kê tập loại thiết bị hỗ trợ.", "List supported device types."),
            ("GET /device-types/{code}", "Lấy thông tin chi tiết theo loại thiết bị.", "Get device-type details."),
            ("GET /device-types/{code}/template", "Lấy template phục vụ import hoặc cấu hình.", "Get a template for import or configuration."),
        ),
    ),
    ApiGroup(
        title_vi="Device action and lifecycle APIs",
        title_en="Device action and lifecycle APIs",
        items=(
            ("POST /devices/{id}/actions/power-on", "Bật thiết bị hoặc đối tượng điều khiển được hỗ trợ.", "Power on a supported device target."),
            ("POST /devices/{id}/actions/power-off", "Tắt thiết bị hoặc đối tượng điều khiển được hỗ trợ.", "Power off a supported device target."),
            ("POST /devices/{id}/actions/dim", "Thiết lập mức dimming.", "Set a dimming level."),
            ("POST /devices/{id}/actions/sync", "Đồng bộ dữ liệu hoặc cấu hình thiết bị.", "Synchronize device data or configuration."),
            ("POST /devices/{id}/actions/reboot", "Khởi động lại thiết bị khi loại thiết bị hỗ trợ.", "Reboot the device when supported."),
            ("POST /devices/{id}/actions/read-data", "Đọc dữ liệu hiện tại từ thiết bị.", "Read current data from the device."),
            ("POST /devices/{deviceId}/control", "Gửi lệnh điều khiển tổng quát.", "Send a generic control command."),
            ("POST /devices/batch", "Tạo thiết bị hàng loạt.", "Create devices in batch."),
            ("POST /devices/batch/import", "Import thiết bị từ file.", "Import devices from a file."),
            ("GET /devices/batch/import/{jobId}", "Theo dõi trạng thái job import.", "Track import job status."),
            ("GET /devices/batch/export", "Xuất danh sách thiết bị.", "Export devices."),
            ("DELETE /devices/batch", "Xóa thiết bị hàng loạt theo danh sách được chọn.", "Delete devices in batch."),
            ("POST /devices/actions/bulk", "Thực thi action hàng loạt.", "Execute a bulk action."),
        ),
    ),
    ApiGroup(
        title_vi="Device group APIs",
        title_en="Device group APIs",
        items=(
            ("GET /device-groups", "Liệt kê group thiết bị.", "List device groups."),
            ("GET /device-groups/{id}", "Lấy thông tin chi tiết group.", "Get device group details."),
            ("POST /device-groups", "Tạo group.", "Create a device group."),
            ("PUT /device-groups/{id}", "Cập nhật group.", "Update a device group."),
            ("DELETE /device-groups/{id}", "Xóa group theo rule nghiệp vụ.", "Delete a device group subject to business rules."),
            ("POST /device-groups/{id}/devices", "Thêm thiết bị vào group.", "Add devices to a group."),
            ("DELETE /device-groups/{id}/devices", "Gỡ thiết bị khỏi group.", "Remove devices from a group."),
            ("POST /device-groups/{id}/sync", "Đồng bộ group hoặc cấu hình multicast.", "Synchronize group or multicast configuration."),
            ("POST /device-groups/{id}/actions/{action}", "Thực thi action ở cấp group.", "Execute a group-level action."),
        ),
    ),
    ApiGroup(
        title_vi="Rule and alarm APIs",
        title_en="Rule and alarm APIs",
        items=(
            ("GET /rules/platform", "Liệt kê platform rules.", "List platform rules."),
            ("POST /rules/platform", "Tạo platform rule.", "Create a platform rule."),
            ("POST /rules/platform/{id}/enable", "Kích hoạt rule.", "Enable a rule."),
            ("POST /rules/platform/{id}/disable", "Vô hiệu hóa rule.", "Disable a rule."),
            ("POST /rules/platform/{id}/execute", "Thực thi rule thủ công.", "Execute a rule manually."),
            ("GET /rules/platform/{id}/executions", "Lấy lịch sử thực thi rule.", "Get rule execution history."),
            ("GET /rules/local", "Liệt kê local rules.", "List local rules."),
            ("POST /rules/local", "Tạo local rule.", "Create a local rule."),
            ("POST /rules/local/{id}/sync", "Đồng bộ local rule xuống thiết bị.", "Synchronize a local rule to the device layer."),
            ("DELETE /rules/local/gateway/{gatewayId}", "Xóa local rules tại gateway khi cần dọn cấu hình.", "Clear local rules at gateway level when required."),
            ("GET /rules/alarm", "Liệt kê alarm rules.", "List alarm rules."),
            ("POST /rules/alarm", "Tạo alarm rule.", "Create an alarm rule."),
            ("GET /alarms", "Liệt kê alarm đang hoạt động hoặc theo bộ lọc.", "List alarms or filtered alarm views."),
            ("POST /alarms/{id}/acknowledge", "Ghi nhận alarm đã được tiếp nhận xử lý.", "Acknowledge an alarm."),
            ("POST /alarms/{id}/resolve", "Đánh dấu alarm đã được xử lý xong.", "Resolve an alarm."),
            ("GET /alarms/statistics", "Lấy số liệu tổng hợp cảnh báo.", "Get alarm statistics."),
        ),
    ),
    ApiGroup(
        title_vi="Dashboard, reporting, and audit APIs",
        title_en="Dashboard, reporting, and audit APIs",
        items=(
            ("GET /dashboard/statistics", "Lấy KPI tổng quan theo project scope.", "Get dashboard KPIs by project scope."),
            ("GET /dashboard/energy", "Lấy dữ liệu energy overview.", "Get energy overview data."),
            ("GET /analytics/energy", "Lấy dữ liệu phân tích điện năng.", "Get energy analytics data."),
            ("GET /dashboard/alarms/summary", "Lấy tổng hợp cảnh báo cho dashboard.", "Get alarm summary information for the dashboard."),
            ("GET /dashboard/devices/status", "Lấy phân bố trạng thái thiết bị.", "Get device status distribution."),
            ("GET /dashboard/map-data", "Lấy dữ liệu hiển thị bản đồ GIS.", "Get GIS map display data."),
            ("GET /recycle-bin", "Liệt kê dữ liệu đã chuyển vào recycle bin.", "List records currently in recycle bin."),
            ("POST /recycle-bin/{id}/restore", "Khôi phục dữ liệu từ recycle bin.", "Restore an item from recycle bin."),
            ("DELETE /recycle-bin/{id}", "Xóa vĩnh viễn một mục khỏi recycle bin.", "Permanently delete a recycle-bin item."),
            ("DELETE /recycle-bin/clear", "Dọn toàn bộ recycle bin.", "Clear the entire recycle bin."),
            ("GET /settings/system", "Lấy cấu hình hệ thống.", "Get system settings."),
            ("PUT /settings/system", "Cập nhật cấu hình hệ thống.", "Update system settings."),
            ("GET /settings/timezone", "Lấy cấu hình timezone.", "Get timezone settings."),
            ("PUT /settings/timezone", "Cập nhật timezone.", "Update timezone settings."),
            ("GET /settings/notifications", "Lấy cấu hình thông báo.", "Get notification settings."),
            ("PUT /settings/notifications", "Cập nhật cấu hình thông báo.", "Update notification settings."),
            ("GET /reports/energy", "Tạo hoặc đọc báo cáo điện năng.", "Read or generate energy reports."),
            ("GET /reports/device-status", "Lấy báo cáo trạng thái thiết bị.", "Get a device-status report."),
            ("GET /reports/alarms", "Lấy báo cáo cảnh báo.", "Get an alarm report."),
            ("GET /reports/operations", "Lấy báo cáo vận hành.", "Get an operations report."),
            ("POST /reports/generate", "Sinh báo cáo tùy biến.", "Generate a custom report."),
            ("GET /reports/{id}/download", "Tải báo cáo đã sinh.", "Download a generated report."),
            ("GET /audit/logs", "Lấy audit logs.", "Get audit logs."),
            ("GET /audit/logs/{id}", "Lấy chi tiết audit log.", "Get audit log details."),
            ("GET /audit/user/{userId}", "Lấy lịch sử hoạt động của một user.", "Get activity history for a user."),
        ),
    ),
)


DIAGRAMS = (
    DiagramSpec(
        key="platform-architecture",
        title_vi="Sơ đồ 1. Kiến trúc nền tảng",
        title_en="Figure 1. Platform architecture",
        caption_vi="Kiến trúc tổng quát của SHUNCOM RULR, kết nối giữa dashboard, API, quản lý thiết bị, rules, project scope và realtime layer.",
        caption_en="High-level SHUNCOM RULR architecture showing the relationship between the dashboard, API, device management, rules, project scope, and the realtime layer.",
        mermaid_vi=textwrap.dedent(
            """
            flowchart TD
                A[Frontend Dashboard] --> B[Backend API]
                B --> C[User & Access]
                B --> D[Project & GIS]
                B --> E[Device Management]
                B --> F[Rule Engine]
                B --> G[Dashboard Analytics & Reports]
                E --> H[IoT Devices]
                F --> H
                H --> I[Realtime Event Stream]
                I --> A
            """
        ).strip(),
        mermaid_en=textwrap.dedent(
            """
            flowchart TD
                A[Frontend Dashboard] --> B[Backend API]
                B --> C[User and Access]
                B --> D[Project and GIS]
                B --> E[Device Management]
                B --> F[Rule Engine]
                B --> G[Dashboard Analytics and Reports]
                E --> H[IoT Devices]
                F --> H
                H --> I[Realtime Event Stream]
                I --> A
            """
        ).strip(),
    ),
    DiagramSpec(
        key="scope-model",
        title_vi="Sơ đồ 2. Mô hình project, sub-project, type, group và device",
        title_en="Figure 2. Project, sub-project, type, group, and device model",
        caption_vi="Project hierarchy là trục vận hành chính; Type và Group là hai chiều phân loại song song dùng để nhìn và vận hành thiết bị.",
        caption_en="The project hierarchy is the primary operating axis, while Type and Group are parallel operational views used to classify and operate devices.",
        mermaid_vi=textwrap.dedent(
            """
            flowchart TD
                A[Organization or Tenant] --> B[Top-level Project]
                B --> C[Sub-project]
                C --> D[Associated Devices]
                C --> E[Dashboard & GIS Context]
                C --> F[Type View]
                C --> G[Group View]
                F --> D
                G --> D
            """
        ).strip(),
        mermaid_en=textwrap.dedent(
            """
            flowchart TD
                A[Organization or Tenant] --> B[Top-level Project]
                B --> C[Sub-project]
                C --> D[Associated Devices]
                C --> E[Dashboard and GIS Context]
                C --> F[Type View]
                C --> G[Group View]
                F --> D
                G --> D
            """
        ).strip(),
    ),
    DiagramSpec(
        key="end-to-end-flow",
        title_vi="Sơ đồ 3. Luồng hoạt động end-to-end",
        title_en="Figure 3. End-to-end operating flow",
        caption_vi="Luồng điển hình từ người dùng đến dashboard, backend API, database, thiết bị thực địa, rule engine và realtime updates.",
        caption_en="Typical operating flow from the end user through the dashboard, backend API, database, field devices, rule engine, and realtime updates.",
        mermaid_vi=textwrap.dedent(
            """
            sequenceDiagram
                participant U as User
                participant D as Dashboard
                participant A as Backend API
                participant DB as Data Layer
                participant DEV as Field Device
                participant R as Rule Engine
                participant RT as Realtime Layer
                U->>D: Đăng nhập và chọn project
                D->>A: Gọi API theo scope
                A->>DB: Đọc hoặc cập nhật dữ liệu
                A->>DEV: Gửi command hoặc sync configuration
                DEV-->>A: Trả về trạng thái hoặc telemetry
                A->>R: Đánh giá rule và alarm logic
                R->>RT: Phát sự kiện realtime
                RT-->>D: Cập nhật dashboard và operation views
            """
        ).strip(),
        mermaid_en=textwrap.dedent(
            """
            sequenceDiagram
                participant U as User
                participant D as Dashboard
                participant A as Backend API
                participant DB as Data Layer
                participant DEV as Field Device
                participant R as Rule Engine
                participant RT as Realtime Layer
                U->>D: Sign in and select a project
                D->>A: Call APIs within scope
                A->>DB: Read or update data
                A->>DEV: Send commands or synchronize configuration
                DEV-->>A: Return status or telemetry
                A->>R: Evaluate rules and alarm logic
                R->>RT: Publish realtime events
                RT-->>D: Refresh dashboard and operation views
            """
        ).strip(),
    ),
    DiagramSpec(
        key="realtime-rule-flow",
        title_vi="Sơ đồ 4. Realtime, cảnh báo và phản hồi vận hành",
        title_en="Figure 4. Realtime, alarm, and operational feedback flow",
        caption_vi="Thiết bị, rule engine, alarm handling và dashboard cùng tham gia vào chu trình phản hồi gần thời gian thực của hệ thống.",
        caption_en="Devices, the rule engine, alarm handling, and the dashboard all participate in the platform's near real-time response cycle.",
        mermaid_vi=textwrap.dedent(
            """
            flowchart LR
                A[Device Telemetry] --> B[Backend API]
                B --> C[Rule Engine]
                C --> D[Alarm Evaluation]
                D --> E[Notification & Maintenance]
                C --> F[Realtime Events]
                B --> F
                F --> G[Dashboard Refresh]
                E --> H[Audit & Reports]
                G --> H
            """
        ).strip(),
        mermaid_en=textwrap.dedent(
            """
            flowchart LR
                A[Device Telemetry] --> B[Backend API]
                B --> C[Rule Engine]
                C --> D[Alarm Evaluation]
                D --> E[Notification and Maintenance]
                C --> F[Realtime Events]
                B --> F
                F --> G[Dashboard Refresh]
                E --> H[Audit and Reports]
                G --> H
            """
        ).strip(),
    ),
)


def l10n(lang: str, vi: str, en: str) -> str:
    return vi if lang == "vi" else en


def bullet_lines(items: Iterable[str]) -> list[dict[str, object]]:
    return [{"type": "bullet", "text": item} for item in items]


def sub_bullet_lines(items: Iterable[str]) -> list[dict[str, object]]:
    return [{"type": "sub-bullet", "text": item} for item in items]


def numbered_lines(items: Iterable[str]) -> list[dict[str, object]]:
    return [{"type": "number", "text": item, "index": index + 1} for index, item in enumerate(items)]


def heading(level: int, text: str) -> dict[str, object]:
    return {"type": f"h{level}", "text": text}


def paragraph(text: str) -> dict[str, object]:
    return {"type": "p", "text": text}


def page_break() -> dict[str, object]:
    return {"type": "page-break"}


def diagram_block(spec: DiagramSpec, lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    title = l10n(lang, spec.title_vi, spec.title_en)
    caption = l10n(lang, spec.caption_vi, spec.caption_en)
    mermaid_code = l10n(lang, spec.mermaid_vi, spec.mermaid_en)
    blocks: list[dict[str, object]] = [heading(3, title)]
    if spec.key in diagram_assets:
        asset = diagram_assets[spec.key]
        blocks.append({"type": "image", "name": asset["name"], "bytes": asset["bytes"], "caption": caption})
    else:
        blocks.append(paragraph(caption))
        blocks.append({"type": "code", "text": mermaid_code})
    return blocks


def build_cover_blocks(lang: str) -> list[dict[str, object]]:
    today = datetime.now().strftime("%Y-%m-%d")
    if lang == "vi":
        return [
            {"type": "cover-title", "text": "SHUNCOM RULR IoT Platform"},
            {"type": "cover-subtitle", "text": "Tài liệu kiến trúc tổng quát, workflow và API reference"},
            {"type": "cover-meta", "text": f"Phiên bản tài liệu: {today}"},
            {"type": "cover-meta", "text": "Đối tượng đọc: Khách hàng, BA, PM, QA, đội triển khai và integration team"},
            {"type": "cover-meta", "text": "Mục đích: cung cấp góc nhìn tổng quát, có cấu trúc và dễ bàn giao về cách hệ thống vận hành"},
            page_break(),
        ]
    return [
        {"type": "cover-title", "text": "SHUNCOM RULR IoT Platform"},
        {"type": "cover-subtitle", "text": "Platform architecture, workflow, and API reference document"},
        {"type": "cover-meta", "text": f"Document version: {today}"},
        {"type": "cover-meta", "text": "Audience: Customers, business analysts, project managers, QA teams, implementation teams, and integration stakeholders"},
        {"type": "cover-meta", "text": "Purpose: provide a structured handover-oriented view of how the platform is organized and operated"},
        page_break(),
    ]


def build_summary_blocks(lang: str) -> list[dict[str, object]]:
    if lang == "vi":
        return [
            heading(1, "1. Executive overview"),
            paragraph("SHUNCOM RULR là nền tảng quản lý IoT tập trung cho các bài toán như smart lighting, gateway control, metering, automation bằng rules, cảnh báo, dashboard vận hành và quản lý thiết bị theo project scope."),
            paragraph("Nền tảng được tổ chức xoay quanh project và sub-project. Từ đó, dashboard, GIS, analytics, rules và operation control đều bám theo cùng một ngữ cảnh quản lý để bảo đảm dữ liệu nhìn thấy và thao tác được luôn nhất quán với quyền truy cập."),
            *bullet_lines(
                (
                    "Project hierarchy là trục tổ chức và điều hành chính của hệ thống.",
                    "Type và Group là hai góc nhìn vận hành song song để phân loại và xử lý thiết bị.",
                    "Device management, rule engine, dashboard và realtime events được kết nối thông qua backend API thống nhất.",
                    "Các API trong tài liệu này nên được dùng như inventory tham chiếu; hợp đồng tích hợp production cần được xác nhận thêm từ backend hoặc OpenAPI chính thức.",
                )
            ),
        ]
    return [
        heading(1, "1. Executive overview"),
        paragraph("SHUNCOM RULR is a centralized IoT platform designed for smart lighting, gateway control, metering, rule-based automation, alarms, operational dashboards, and project-scoped device management."),
        paragraph("The platform is organized around projects and sub-projects. From this hierarchy, dashboards, GIS views, analytics, rules, and operation control all inherit a consistent management context so that visibility and actions remain aligned with access rights."),
        *bullet_lines(
            (
                "The project hierarchy is the primary organizational and operational axis of the platform.",
                "Type and Group are parallel operational views used to classify and manage devices.",
                "Device management, the rule engine, dashboards, and realtime events are connected through a unified backend API layer.",
                "The APIs in this document should be used as a reference inventory; production integration contracts should be confirmed against backend or official OpenAPI sources.",
            )
        ),
    ]


def build_architecture_blocks(lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    if lang == "vi":
        blocks = [
            heading(1, "2. Kiến trúc nền tảng"),
            paragraph("Ở mức tổng quát, SHUNCOM RULR gồm lớp dashboard phía người dùng, backend API, lớp quản lý thiết bị, rule engine, project and GIS layer, cùng kênh realtime để phản hồi trạng thái vận hành."),
            *diagram_block(DIAGRAMS[0], lang, diagram_assets),
            paragraph("Backend API đóng vai trò lõi tích hợp. Từ đây, hệ thống quản lý xác thực, phân quyền, project hierarchy, cấu hình thiết bị, automation, alarm handling và dữ liệu dashboard theo cùng một chuẩn giao tiếp."),
            paragraph("Realtime layer giúp đưa các thay đổi trạng thái thiết bị, alarm events và rule executions về dashboard gần thời gian thực, hỗ trợ đội vận hành theo dõi và phản ứng nhanh hơn."),
        ]
    else:
        blocks = [
            heading(1, "2. Platform architecture"),
            paragraph("At a high level, SHUNCOM RULR combines a user-facing dashboard layer, a backend API, device management services, a rule engine, a project and GIS layer, and a realtime channel for operational feedback."),
            *diagram_block(DIAGRAMS[0], lang, diagram_assets),
            paragraph("The backend API acts as the central integration layer. It coordinates authentication, access control, project hierarchy, device configuration, automation, alarm handling, and dashboard data through one consistent interaction model."),
            paragraph("The realtime layer brings device-state changes, alarm events, and rule execution feedback back to the dashboard in near real time so that operations teams can monitor and respond more effectively."),
        ]
    return blocks


def build_scope_blocks(lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    if lang == "vi":
        blocks = [
            heading(1, "3. Mô hình project, sub-project, type, group và device"),
            paragraph("Mô hình vận hành của nền tảng đặt project hierarchy ở vị trí trung tâm. Type và Group không thay thế project tree mà đóng vai trò là hai lớp nhìn và vận hành song song trong cùng một phạm vi project."),
            *diagram_block(DIAGRAMS[1], lang, diagram_assets),
            *bullet_lines(
                (
                    "Top-level project thường là container cấp cao cho tổ chức hoặc đơn vị quản lý.",
                    "Sub-project là phạm vi vận hành chính cho dashboard, GIS, analytics và rules.",
                    "Type view hỗ trợ tổ chức thiết bị theo category hoặc product logic.",
                    "Group view hỗ trợ vận hành theo nhóm, multicast hoặc mục tiêu xử lý nghiệp vụ.",
                    "Trong tài liệu tiếng Việt này, Group được diễn giải kèm theo ngữ cảnh Zone khi mô tả tổ chức thiết bị và phạm vi vận hành.",
                    "Mỗi thiết bị có thể đồng thời mang context theo project, type, group và management scope.",
                )
            ),
            paragraph("Cách tổ chức này giúp cùng một thiết bị có thể được nhìn dưới nhiều góc độ mà không làm mất đi tính nhất quán của phạm vi quản lý và phân quyền hiển thị dữ liệu."),
        ]
    else:
        blocks = [
            heading(1, "3. Project, sub-project, type, group, and device model"),
            paragraph("The operating model places the project hierarchy at the center. Type and Group do not replace the project tree; instead, they provide two parallel operating views inside the same project scope."),
            *diagram_block(DIAGRAMS[1], lang, diagram_assets),
            *bullet_lines(
                (
                    "The top-level project usually acts as the upper management container for an organization or operating unit.",
                    "A sub-project becomes the main operating scope for dashboards, GIS, analytics, and rules.",
                    "The Type view organizes devices by category or product logic.",
                    "The Group view supports grouped operation, multicast behavior, and business-specific targeting.",
                    "A single device may simultaneously carry project, type, group, and management-scope context.",
                )
            ),
            paragraph("This model allows the same device to be viewed from multiple operational angles without losing consistency in data visibility and access control."),
        ]
    return blocks


def build_role_blocks(lang: str) -> list[dict[str, object]]:
    if lang != "vi":
        return []
    return [
        heading(1, "4. Phân quyền và phạm vi quản lý"),
        paragraph("Mô hình phân quyền chuẩn của hệ thống được tổ chức theo 3 nhóm chính: Manufacturer, Project Admin và Project Member. Quyền hiển thị dữ liệu và quyền thao tác luôn phụ thuộc đồng thời vào role và phạm vi project đang được giao."),
        heading(2, "4.1 Vai trò chuẩn"),
        *bullet_lines(
            (
                "Manufacturer: hiển thị toàn bộ area, project, zone/group, device và có toàn quyền ở cấp nền tảng.",
                "Project Admin: có toàn quyền trong project hoặc nhóm project đang được giao quản lý; chịu trách nhiệm cấu hình project, membership, thiết bị, rules, dashboard và vận hành trong phạm vi đó.",
                "Project Member: quyền được Project Admin cấu hình; chỉ tồn tại trong phạm vi project được gán và có thể đóng vai viewer, operator, engineer hoặc analyst tùy cấu hình.",
            )
        ),
        heading(2, "4.2 Ma trận quản lý và quyền chính"),
        *bullet_lines(
            (
                "Manufacturer — quản lý: tất cả area / project / zone-group / device / rules / alarms / dashboard / báo cáo / membership trên toàn hệ thống.",
                "Project Admin — quản lý: toàn bộ resource trong project do mình phụ trách, gồm devices, rules, alarms, dashboard, reports, logs và project membership trong project đó.",
                "Project Member — quản lý: chỉ các tính năng và dữ liệu do Project Admin cấu hình cho phép trong cùng project scope; không có quyền vượt ra ngoài project được gán.",
            )
        ),
        heading(2, "4.3 Chi tiết theo nhóm quyền"),
        *bullet_lines(
            (
                "Area / Project / Zone: Manufacturer nhìn và quản lý toàn bộ; Project Admin toàn quyền trong project mình quản lý; Project Member chỉ nhìn thấy phần được cấp.",
                "Devices: Manufacturer và Project Admin có thể xem, tạo, sửa, xóa, import/export và thực thi command trong phạm vi tương ứng; Project Member là configurable theo delegated scope.",
                "Rules và alarms: Manufacturer và Project Admin có thể xem, tạo, chỉnh sửa, enable/disable, execute và xử lý cảnh báo trong phạm vi của mình; Project Member nhận quyền theo cấu hình Project Admin.",
                "Dashboard / Reports / Logs: Manufacturer có quyền toàn hệ thống; Project Admin có quyền trong project; Project Member có thể được cấp quyền xem, export hoặc thao tác hạn chế tùy cấu hình.",
                "Project membership: chỉ Manufacturer và Project Admin được tạo, sửa, xóa Project Member và thay đổi permission set trong phạm vi hợp lệ.",
            )
        ),
        paragraph("Nguyên tắc chính là Manufacturer là role toàn cục duy nhất; Project Admin mạnh trong project scope; Project Member là role dạng permission envelope do Project Admin cấu hình, không phải top-level role độc lập mới."),
    ]


def build_device_blocks(lang: str) -> list[dict[str, object]]:
    blocks = [heading(1, l10n(lang, "5. Supported device types", "4. Supported device types"))]
    intro = l10n(
        lang,
        "Phần này giải thích các loại thiết bị đang được mô tả trong markdown hiện có của dự án. Với bản tiếng Việt, nội dung được mở rộng theo hướng tài liệu bàn giao cho khách hàng và tài liệu nghiệp vụ cho UI/backend alignment.",
        "This section explains the device types currently documented in the project's markdown sources. The descriptions are customer-oriented and focus on business role, deployment context, key configuration dependencies, and operational notes.",
    )
    blocks.append(paragraph(intro))
    if lang == "vi":
        blocks.append(paragraph("Mọi biểu mẫu tạo thiết bị đều xoay quanh 3 nhóm dữ liệu chính: Device Information, Product Information và Asset Information. Product thường là bắt buộc; device number bắt buộc trong hầu hết trường hợp trừ khi logic sản phẩm tự sinh; project, group/zone và location phụ thuộc theo từng loại thiết bị."))
        blocks.append(heading(2, "5.1 Khung dữ liệu dùng chung cho UI -> backend"))
        blocks.extend(
            bullet_lines(
                (
                    "Device Information: device_name, product_name, device_number, project_id, belonging_group (Group = Zone), latitude, longitude, altitude và các association theo loại thiết bị.",
                    "Product Information: khối thông tin chi tiết của device, có thể nhập tay từng field hoặc import từ file theo chiến lược triển khai UI.",
                    "Asset Information: manufacturer, price, purchase_date, installation_date, expiration_date, expiration_of_tariff, service_life, type, function và các trường vòng đời tài sản khác nếu UI hỗ trợ.",
                )
            )
        )
    for device in DEVICES:
        blocks.append(heading(2, device.name))
        blocks.extend(
            bullet_lines(
                (
                    l10n(lang, f"Purpose: {device.purpose_vi}", f"Purpose: {device.purpose_en}"),
                    l10n(lang, f"Typical deployment: {device.deployment_vi}", f"Typical deployment: {device.deployment_en}"),
                    l10n(lang, f"Key configuration notes: {device.configuration_vi}", f"Key configuration notes: {device.configuration_en}"),
                    l10n(lang, f"Operational notes: {device.operations_vi}", f"Operational notes: {device.operations_en}"),
                )
            )
        )
        if lang == "vi" and device.name == "Gateway":
            blocks.append(paragraph("Gateway là mẫu tham chiếu rõ nhất cho kiểu biểu mẫu cấu hình thiết bị hiện tại. Các field dưới đây là các trường UI cần thu thập và gửi xuống backend ở mức nghiệp vụ/tài liệu thiết kế."))
            blocks.extend(
                bullet_lines(
                    (
                        "Device name — tên thiết bị hiển thị trên UI.",
                        "Product name — tên hoặc mã sản phẩm, là trường bắt buộc.",
                        "Device number — mã định danh thiết bị; theo một số nguồn có thể được dùng như MAC address hoặc identifier chính.",
                        "Lat and Long — kinh độ, vĩ độ của vị trí lắp đặt; dùng cho GIS, dashboard map và các use case sunrise/sunset.",
                        "Mac Address — nên được mô tả như identifier hoặc mapping của device number nếu backend đang dùng MAC làm số thiết bị.",
                        "Project — project_id hoặc parent project assignment.",
                        "Group = Zone — belonging_group trong UI tiếng Việt nên note rõ là zone/group vận hành.",
                    )
                )
            )
            blocks.append(paragraph("Khối Product Information cho Gateway"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "Device Manufacturer — text",
                        "Product model — text",
                        "Supply Voltage — text",
                        "Overall Power Consumption — text",
                        "Product Image — image",
                        "Product Introduction — text",
                        "UI có thể hỗ trợ delete field hoặc select all field cho khối này nếu chiến lược sản phẩm yêu cầu nhập động/import động.",
                    )
                )
            )
            blocks.append(paragraph("Khối Asset Information cho Gateway"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "manufacturer — string",
                        "price — number",
                        "purchase_date — date",
                        "installation_date — date",
                        "expiration_date — date",
                        "expiration_of_tariff — date",
                        "service_life — number",
                        "type — string",
                        "function — string",
                    )
                )
            )
        if lang == "vi" and device.name == "Industrial Controller":
            blocks.append(paragraph("Industrial Controller hiện chưa có flow canonical chi tiết riêng bằng Gateway hoặc Smart Light Controller. Trong tài liệu bàn giao này, có thể xem nó dùng cùng khung thông tin cơ sở như Gateway trừ khi product model thực tế yêu cầu field đặc thù riêng."))
            blocks.extend(
                bullet_lines(
                    (
                        "Device name",
                        "Product name",
                        "Device number",
                        "Latitude / Longitude / Altitude nếu cần theo vị trí lắp đặt",
                        "Project",
                        "Group = Zone",
                        "Product Information block theo product model",
                        "Asset Information block theo chuẩn vòng đời tài sản",
                    )
                )
            )
        if lang == "vi" and device.name == "Smart Light Controller":
            blocks.append(paragraph("Smart Light Controller là thiết bị có logic field động rõ nhất. UI cần render field theo device_type hoặc subtype, và payload gửi xuống backend phải thay đổi theo giao thức truyền thông tương ứng."))
            blocks.append(paragraph("1. Device type / subtype"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "device_type (enum, required)",
                        "zigbee_v3",
                        "dual_way_zigbee_v3",
                        "nb_iot",
                        "cat1",
                        "lora",
                    )
                )
            )
            blocks.append(paragraph("2. Common fields áp dụng cho toàn bộ Smart Light Controller"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "device_name — string, optional",
                        "product_name — string, required",
                        "light_pole_id — string, optional",
                        "associated_luminaires — string[], optional nhưng có thể bắt buộc theo subtype điều khiển đèn",
                        "project_id — string, optional",
                        "latitude — number, optional",
                        "longitude — number, optional",
                        "altitude — number, optional",
                        "belonging_group — string, optional, note Group = Zone",
                    )
                )
            )
            blocks.append(paragraph("3. Pass-through devices (Zigbee)"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "Condition: device_type IN (zigbee_v3, dual_way_zigbee_v3)",
                        "device_number — required",
                        "gateway_id — required",
                    )
                )
            )
            blocks.append(paragraph("4. Directly communicated devices (NB-IoT / CAT.1)"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "Condition: device_type IN (nb_iot, cat1)",
                        "device_number — required",
                        "gateway_id — không yêu cầu",
                    )
                )
            )
            blocks.append(paragraph("5. LoRa Light Controller"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "Common LoRa fields: devui, dev_profile, access_mode",
                        "Nếu access_mode = OTAA: appkey là required",
                        "Nếu access_mode = ABP: devaddr, nwkskey là required",
                        "Tuỳ model thực tế có thể cần thêm appskey hoặc các network keys khác; cần xác nhận lại với backend/product source nếu dùng làm contract cuối cùng.",
                    )
                )
            )
            blocks.append(paragraph("6. Asset Information (optional)"))
            blocks.extend(
                sub_bullet_lines(
                    (
                        "manufacturer",
                        "price",
                        "purchase_date",
                        "installation_date",
                        "expiration_date",
                        "expiration_of_tariff",
                        "service_life",
                        "type",
                        "function",
                    )
                )
            )
    return blocks


def build_workflow_blocks(lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    blocks = [heading(1, l10n(lang, "6. Core workflows", "5. Core workflows"))]
    blocks.append(
        paragraph(
            l10n(
                lang,
                "Các workflow dưới đây mô tả cách các module chính của SHUNCOM RULR phối hợp với nhau trong quá trình vận hành và cấu hình hệ thống.",
                "The workflows below describe how the main SHUNCOM RULR modules work together during platform operation and configuration.",
            )
        )
    )
    blocks.extend(diagram_block(DIAGRAMS[2], lang, diagram_assets))
    for workflow in WORKFLOWS:
        blocks.append(heading(2, l10n(lang, workflow.title_vi, workflow.title_en)))
        blocks.append(paragraph(l10n(lang, f"Mục tiêu: {workflow.objective_vi}", f"Objective: {workflow.objective_en}")))
        blocks.extend(numbered_lines(l10n(lang, workflow.steps_vi, workflow.steps_en)))
        blocks.append(paragraph(l10n(lang, "API liên quan:", "Related APIs:")))
        blocks.extend(bullet_lines(workflow.apis))
    return blocks


def build_api_blocks(lang: str) -> list[dict[str, object]]:
    if lang == "vi":
        blocks = [
            heading(1, "7. API reference inventory"),
            paragraph("Danh sách dưới đây nên được dùng như inventory tham chiếu để phục vụ review giải pháp, traceability và chuẩn bị integration. Trước khi dùng làm contract production, tên endpoint, payload, permission keys và hành vi realtime cần được xác nhận lại với backend implementation hoặc OpenAPI chính thức."),
            *bullet_lines(
                (
                    "REST base URL tham chiếu: https://rulr-aiot.com/api/v1",
                    "Realtime base URL tham chiếu: wss://rulr-aiot.com/ws/v1",
                    "Auth model: Bearer token cho các tài nguyên được bảo vệ",
                    "Scope model: role + management scope + project/group/device visibility",
                )
            ),
        ]
    else:
        blocks = [
            heading(1, "6. API reference inventory"),
            paragraph("The following list should be used as a reference inventory for solution review, traceability, and integration preparation. Before it is used as a production contract, endpoint names, payloads, permission keys, and realtime behavior should be validated against the backend implementation or official OpenAPI source."),
            *bullet_lines(
                (
                    "Reference REST base URL: https://rulr-aiot.com/api/v1",
                    "Reference realtime base URL: wss://rulr-aiot.com/ws/v1",
                    "Authentication model: Bearer token for protected resources",
                    "Scope model: role + management scope + project/group/device visibility",
                )
            ),
        ]
    for group in API_GROUPS:
        blocks.append(heading(2, l10n(lang, group.title_vi, group.title_en)))
        for path, vi_desc, en_desc in group.items:
            blocks.append({"type": "api", "path": path, "desc": l10n(lang, vi_desc, en_desc)})
    return blocks


def build_realtime_blocks(lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    if lang == "vi":
        blocks = [
            heading(1, "8. Realtime, alarms và phản hồi vận hành"),
            paragraph("Ngoài các API đọc/ghi dữ liệu, SHUNCOM RULR còn dựa trên kênh realtime để đẩy trạng thái thiết bị, alarm events, rule executions và dashboard refresh về phía người dùng vận hành."),
            *diagram_block(DIAGRAMS[3], lang, diagram_assets),
            paragraph("Các topic hoặc message groups thường được tài liệu hiện tại tham chiếu gồm device status updates, per-device metrics, alarm notifications, rule execution feedback và dashboard statistics updates."),
            *bullet_lines(
                (
                    "device.status hoặc device.status.update",
                    "devices.{id}.metrics",
                    "alarms, alarm.triggered, alarms.new",
                    "rules, rule.executed, rules.execution",
                    "dashboard.statistics",
                )
            ),
        ]
    else:
        blocks = [
            heading(1, "7. Realtime, alarms, and operational feedback"),
            paragraph("In addition to data-oriented APIs, SHUNCOM RULR relies on a realtime channel to deliver device status, alarm events, rule execution feedback, and dashboard refresh updates to operations users."),
            *diagram_block(DIAGRAMS[3], lang, diagram_assets),
            paragraph("The current documentation refers to message groups such as device status updates, per-device metrics, alarm notifications, rule execution feedback, and dashboard statistics updates."),
            *bullet_lines(
                (
                    "device.status or device.status.update",
                    "devices.{id}.metrics",
                    "alarms, alarm.triggered, alarms.new",
                    "rules, rule.executed, rules.execution",
                    "dashboard.statistics",
                )
            ),
        ]
    return blocks


def build_constraints_blocks(lang: str) -> list[dict[str, object]]:
    if lang == "vi":
        return [
            heading(1, "9. Business constraints and document notes"),
            *bullet_lines(
                (
                    "Hầu hết API ngoài authentication đều cần role, permission và management scope phù hợp.",
                    "Validation thiết bị phụ thuộc loại thiết bị, product và subtype được chọn.",
                    "Timezone ảnh hưởng trực tiếp đến các rule time-based và lịch vận hành.",
                    "Dữ liệu tọa độ là điều kiện quan trọng cho GIS distribution và các use case sunrise/sunset.",
                    "Batch import đang được tài liệu hiện có mô tả ở mức hỗ trợ tới 5.000 bản ghi mỗi đợt.",
                    "Delete và recycle flows cần được cân nhắc cùng các dependency bindings và lịch sử dữ liệu liên quan.",
                )
            ),
            paragraph("Tài liệu này được biên soạn theo hướng bàn giao và giải thích hệ thống cho khách hàng. Một số chi tiết kỹ thuật trong phần API vẫn mang tính tham chiếu từ tài liệu phân tích hiện có; vì vậy cần xác nhận thêm trước khi sử dụng như ràng buộc tích hợp production."),
        ]
    return [
        heading(1, "8. Business constraints and document notes"),
        *bullet_lines(
            (
                "Most APIs outside authentication require the appropriate role, permission, and management scope.",
                "Device validation depends on the selected device type, product, and subtype.",
                "Timezone directly affects time-based rules and operating schedules.",
                "Coordinate data is important for GIS distribution and sunrise/sunset-based use cases.",
                "Current documentation describes batch import support at up to 5,000 records per batch.",
                "Delete and recycle flows must be considered together with dependency bindings and related historical data.",
            )
        ),
        paragraph("This document has been prepared as a customer-facing handover and explanation package. Some technical details in the API section are still reference-oriented and should be validated before they are treated as production integration commitments."),
    ]


def build_document_blocks(lang: str, diagram_assets: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    return [
        *build_cover_blocks(lang),
        *build_summary_blocks(lang),
        *build_architecture_blocks(lang, diagram_assets),
        *build_scope_blocks(lang, diagram_assets),
        *build_role_blocks(lang),
        *build_device_blocks(lang),
        *build_workflow_blocks(lang, diagram_assets),
        *build_api_blocks(lang),
        *build_realtime_blocks(lang, diagram_assets),
        *build_constraints_blocks(lang),
    ]


def run_xml(text: str, *, bold: bool = False, italic: bool = False, size: int = 22, font: str = "Calibri", color: str | None = None) -> str:
    text = escape(text)
    parts = [
        f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}"/>',
        f'<w:sz w:val="{size}"/>',
        f'<w:szCs w:val="{size}"/>',
    ]
    if bold:
        parts.append("<w:b/>")
    if italic:
        parts.append("<w:i/>")
    if color:
        parts.append(f'<w:color w:val="{color}"/>')
    return f'<w:r><w:rPr>{"".join(parts)}</w:rPr><w:t xml:space="preserve">{text}</w:t></w:r>'


def paragraph_xml(
    text: str,
    *,
    bold: bool = False,
    italic: bool = False,
    size: int = 22,
    font: str = "Calibri",
    indent: int = 0,
    spacing_after: int = 120,
    spacing_before: int = 0,
    align: str | None = None,
    color: str | None = None,
) -> str:
    if text == "":
        return "<w:p/>"
    ppr = [f'<w:spacing w:before="{spacing_before}" w:after="{spacing_after}"/>']
    if indent:
        ppr.append(f'<w:ind w:left="{indent}"/>')
    if align:
        ppr.append(f'<w:jc w:val="{align}"/>')
    ppr_xml = f'<w:pPr>{"".join(ppr)}</w:pPr>'
    return f'<w:p>{ppr_xml}{run_xml(text, bold=bold, italic=italic, size=size, font=font, color=color)}</w:p>'


def page_break_xml() -> str:
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def code_paragraph_xml(text: str) -> str:
    return paragraph_xml(text, size=18, font="Consolas", spacing_after=0)


def get_png_dimensions(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Unsupported image format; expected PNG")
    return struct.unpack(">II", data[16:24])


def scaled_image_extent(width_px: int, height_px: int) -> tuple[int, int]:
    width_emu = width_px * EMU_PER_PIXEL
    height_emu = height_px * EMU_PER_PIXEL
    if width_emu <= MAX_IMAGE_WIDTH_EMU:
        return width_emu, height_emu
    scale = MAX_IMAGE_WIDTH_EMU / width_emu
    return int(width_emu * scale), int(height_emu * scale)


def image_paragraph_xml(rel_id: str, doc_pr_id: int, name: str, width_px: int, height_px: int) -> str:
    width_emu, height_emu = scaled_image_extent(width_px, height_px)
    return (
        "<w:p>"
        "<w:pPr><w:spacing w:before=\"120\" w:after=\"80\"/><w:jc w:val=\"center\"/></w:pPr>"
        "<w:r><w:drawing>"
        f"<wp:inline distT=\"0\" distB=\"0\" distL=\"0\" distR=\"0\" xmlns:wp=\"{NS_WP}\">"
        f"<wp:extent cx=\"{width_emu}\" cy=\"{height_emu}\"/>"
        f"<wp:docPr id=\"{doc_pr_id}\" name=\"{escape(name)}\"/>"
        "<wp:cNvGraphicFramePr/>"
        f"<a:graphic xmlns:a=\"{NS_A}\">"
        "<a:graphicData uri=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        f"<pic:pic xmlns:pic=\"{NS_PIC}\">"
        f"<pic:nvPicPr><pic:cNvPr id=\"0\" name=\"{escape(name)}\"/><pic:cNvPicPr/></pic:nvPicPr>"
        f"<pic:blipFill><a:blip r:embed=\"{rel_id}\" xmlns:r=\"{NS_R}\"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>"
        f"<pic:spPr><a:xfrm><a:off x=\"0\" y=\"0\"/><a:ext cx=\"{width_emu}\" cy=\"{height_emu}\"/></a:xfrm><a:prstGeom prst=\"rect\"><a:avLst/></a:prstGeom></pic:spPr>"
        "</pic:pic>"
        "</a:graphicData></a:graphic>"
        "</wp:inline>"
        "</w:drawing></w:r></w:p>"
    )


def render_document_xml(blocks: list[dict[str, object]]) -> tuple[str, list[tuple[str, bytes]]]:
    paragraphs: list[str] = []
    media_items: list[tuple[str, bytes]] = []
    image_counter = 1
    for block in blocks:
        block_type = block["type"]
        if block_type == "cover-title":
            paragraphs.append(paragraph_xml(block["text"], bold=True, size=34, align="center", spacing_before=600, spacing_after=240, color="1F4E79"))
        elif block_type == "cover-subtitle":
            paragraphs.append(paragraph_xml(block["text"], italic=True, size=24, align="center", spacing_after=200, color="44546A"))
        elif block_type == "cover-meta":
            paragraphs.append(paragraph_xml(block["text"], size=20, align="center", spacing_after=80, color="595959"))
        elif block_type == "h1":
            paragraphs.append(paragraph_xml(block["text"], bold=True, size=28, spacing_before=240, spacing_after=160, color="1F1F1F"))
        elif block_type == "h2":
            paragraphs.append(paragraph_xml(block["text"], bold=True, size=24, spacing_before=180, spacing_after=120, color="1F1F1F"))
        elif block_type == "h3":
            paragraphs.append(paragraph_xml(block["text"], bold=True, size=21, spacing_before=120, spacing_after=100, color="2F5597"))
        elif block_type == "p":
            paragraphs.append(paragraph_xml(block["text"], size=21, spacing_after=100))
        elif block_type == "bullet":
            paragraphs.append(paragraph_xml(f"• {block['text']}", size=21, indent=360, spacing_after=60))
        elif block_type == "sub-bullet":
            paragraphs.append(paragraph_xml(f"- {block['text']}", size=20, indent=720, spacing_after=40))
        elif block_type == "number":
            paragraphs.append(paragraph_xml(f"{block['index']}. {block['text']}", size=21, indent=360, spacing_after=60))
        elif block_type == "api":
            api_text = f"{block['path']} — {block['desc']}"
            paragraphs.append(paragraph_xml(api_text, size=20, indent=360, spacing_after=50))
        elif block_type == "code":
            paragraphs.append(code_paragraph_xml("```mermaid"))
            for line in str(block["text"]).splitlines():
                paragraphs.append(code_paragraph_xml(line))
            paragraphs.append(code_paragraph_xml("```"))
        elif block_type == "image":
            media_name = f"image{image_counter}.png"
            image_bytes = block["bytes"]
            width_px, height_px = get_png_dimensions(image_bytes)
            paragraphs.append(image_paragraph_xml(f"rIdImage{image_counter}", image_counter + 100, block["name"], width_px, height_px))
            paragraphs.append(paragraph_xml(block["caption"], italic=True, size=18, align="center", spacing_after=140, color="666666"))
            media_items.append((media_name, image_bytes))
            image_counter += 1
        elif block_type == "page-break":
            paragraphs.append(page_break_xml())
    sect = (
        '<w:sectPr>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1440" w:right="1134" w:bottom="1440" w:left="1134" w:header="708" w:footer="708" w:gutter="0"/>'
        '</w:sectPr>'
    )
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{NS_W}" xmlns:r="{NS_R}" xmlns:wp="{NS_WP}" xmlns:a="{NS_A}" xmlns:pic="{NS_PIC}">'
        '<w:body>' + ''.join(paragraphs) + sect + '</w:body></w:document>'
    )
    return document_xml, media_items


def build_document_rels(media_items: list[tuple[str, bytes]]) -> str:
    relationships = []
    for index, (media_name, _data) in enumerate(media_items, start=1):
        relationships.append(
            f'<Relationship Id="rIdImage{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{media_name}"/>'
        )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + ''.join(relationships)
        + '</Relationships>'
    )


def build_content_types(has_png: bool) -> str:
    png_default = '<Default Extension="png" ContentType="image/png"/>' if has_png else ''
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        f'{png_default}'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
        '</Types>'
    )


def package_docx(output_path: Path, lang: str, document_xml: str, media_items: list[tuple[str, bytes]]) -> None:
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    title = "SHUNCOM RULR IoT Platform Reference" if lang == "en" else "Tài liệu SHUNCOM RULR IoT Platform"
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
        '</Relationships>'
    )
    core = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f'<dc:title>{escape(title)}</dc:title>'
        '<dc:creator>Claude Code</dc:creator>'
        '<cp:lastModifiedBy>Claude Code</cp:lastModifiedBy>'
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>'
        '</cp:coreProperties>'
    )
    app = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        '<Application>Claude Code</Application>'
        '</Properties>'
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", build_content_types(bool(media_items)))
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("docProps/core.xml", core)
        archive.writestr("docProps/app.xml", app)
        archive.writestr("word/document.xml", document_xml)
        archive.writestr("word/_rels/document.xml.rels", build_document_rels(media_items))
        for media_name, image_bytes in media_items:
            archive.writestr(f"word/media/{media_name}", image_bytes)


def render_mermaid_diagrams(lang: str) -> dict[str, dict[str, object]]:
    assets: dict[str, dict[str, object]] = {}
    npx = shutil.which("npx.cmd") or shutil.which("npx")
    if not npx:
        return assets
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        puppeteer_config = temp_dir / "puppeteer-config.json"
        puppeteer_config.write_text(json.dumps({"args": ["--no-sandbox"]}), encoding="utf-8")
        for spec in DIAGRAMS:
            source_path = temp_dir / f"{spec.key}-{lang}.mmd"
            output_path = temp_dir / f"{spec.key}-{lang}.png"
            mermaid_text = l10n(lang, spec.mermaid_vi, spec.mermaid_en)
            source_path.write_text(mermaid_text, encoding="utf-8")
            command = [
                npx,
                "--yes",
                "@mermaid-js/mermaid-cli",
                "-i",
                str(source_path),
                "-o",
                str(output_path),
                "-t",
                "neutral",
                "-b",
                "white",
                "--scale",
                "2",
                "--puppeteerConfigFile",
                str(puppeteer_config),
            ]
            try:
                subprocess.run(command, check=True, capture_output=True, text=True)
            except Exception:
                continue
            if output_path.exists():
                assets[spec.key] = {"name": output_path.name, "bytes": output_path.read_bytes()}
    return assets


def build_and_write_docx(lang: str) -> tuple[Path, bool]:
    diagram_assets = render_mermaid_diagrams(lang)
    blocks = build_document_blocks(lang, diagram_assets)
    document_xml, media_items = render_document_xml(blocks)
    output_path = OUTPUTS[lang]
    package_docx(output_path, lang, document_xml, media_items)
    diagrams_embedded = len(diagram_assets) == len(DIAGRAMS)
    return output_path, diagrams_embedded


def main() -> None:
    results = []
    for lang in ("vi", "en"):
        path, diagrams_embedded = build_and_write_docx(lang)
        results.append((lang, path, diagrams_embedded))
    for lang, path, diagrams_embedded in results:
        print(f"[{lang}] {path}")
        print(f"[{lang}] diagrams_embedded={diagrams_embedded}")
        print(f"[{lang}] size={path.stat().st_size}")


if __name__ == "__main__":
    main()
