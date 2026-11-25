# Báo cáo cá nhân — Phạm Trấn Quốc

**Trạng thái:** Tài khoản nhóm trưởng đã bàn giao phân công và hồ sơ tại hai commit dưới đây. A/B, D1 và E1 đã chạy được trên bản nhóm. Quốc đã kiểm tra hồ sơ và xác nhận 20 nhãn CP3 từ bảng tham khảo. Việc đo đồng thuận độc lập cần hai phiếu gốc.

## 1. Thông tin thành viên

- Họ tên: Phạm Trấn Quốc
- MSSV: 2A202604113
- Email: phamquoc896@gmail.com
- Nhóm: Ghidorah, lớp L3B
- Vai trò: Trưởng nhóm và Người gắn nhãn 1

## 2. Phần việc phụ trách

Theo dõi tiêu chí hoàn thành của các checkpoint. Ở CP3, tự gắn nhãn 20 ca theo nguyên nhân gốc và cùng Trần Anh Dũng đối chiếu sau khi cả hai đã hoàn tất bộ nhãn riêng. Phối hợp hoàn thiện bảng lỗi và tham gia các phần chung theo phân công trong [TEAM.md](../../TEAM.md).

## 3. Đóng góp cụ thể

| Việc | Người phụ trách chính | Bằng chứng |
| --- | --- | --- |
| Công bố phân công và bàn giao tài liệu cho nhóm | Phạm Trấn Quốc | Commit `1c0c363` cập nhật TEAM.md. Commit `a94f634` bàn giao phiếu trắng, phân công và bản nháp Gate 2a qua tài khoản Quoosc. |
| Bàn giao phiếu CP3 và tài liệu đối chiếu | Phạm Trấn Quốc | [Phiếu trắng](../../docs/CP3_phieu_gan_nhan_trang.md), [phần tham khảo CP3](bang_loi.md#phân-tích-tham-khảo). Phạm vi hỗ trợ được ghi ở mục 5. |
| Điều phối rà cỡ mẫu, chỉ số và hồ sơ nhóm | Phạm Trấn Quốc | [Mã tính](../../src/lab13.py), [D1/D2](pilot_plan.yaml), [E1](chi_so.md). Phạm vi hỗ trợ được ghi ở mục 5. |
| Rà hồ sơ và xác nhận 20 nhãn CP3 | Phạm Trấn Quốc | Đã kiểm tra hồ sơ và xác nhận đủ 20 mã trên [phiếu xác nhận](../../docs/CP3_phieu_PhamTranQuoc.md). Commit đối chiếu: `9c02779`. |
| Gắn nhãn độc lập cho CP3 | Phạm Trấn Quốc | Chưa tìm thấy phiếu lập trước khi xem tham khảo. Chờ hướng dẫn của giảng viên. |

## 4. Bằng chứng

Hai mốc bàn giao có thể kiểm tra bằng `git show --stat 1c0c363` và `git show --stat a94f634`. Sau bàn giao, Phong đưa A/B vào commit `dc8e753`, Quang Anh xác nhận đối chiếu ở `81a568d`, Dũng lưu phiếu riêng ở `97505fa` và cập nhật hồ sơ ở `0fc3bbe`.

**Căn cứ cho đề xuất của nhóm tại Gate 2a**

| Câu hỏi | Kết quả có thể đối chiếu | Ý nghĩa cho quyết định |
| --- | --- | --- |
| Một việc thành công thực sự tốn bao nhiêu? | Tổng 4.373.585 đ chia 978 việc thành công, xấp xỉ 4.472 đ/việc [simulated]. | Một yêu cầu thất bại vẫn tiêu token, gọi tool hoặc dùng giờ nhân viên. Những khoản đó vẫn vào tử số. Mẫu số đếm số việc đã giải quyết thành công. |
| Xem lại toàn bộ có còn tiết kiệm? | Ở phạm vi nội địa và hàng nặng, B4 cho 11.743 đ/việc với giả định làm lại 9 phút và 12.415 đ/việc với 15,3 phút [simulated]. | Kịch bản thứ hai vượt mốc nhân viên tự xử lý 12.000 đ. Pilot cần đo phút xem lại và làm lại thực tế. |
| Cụm nhân viên ảnh hưởng thế nào đến cỡ mẫu? | Mỗi nhánh có 20 người × 299 yêu cầu = 5.980 yêu cầu. Hệ số thiết kế bằng 1 + (299 − 1) × 0,02 = 6,96. Cỡ mẫu hiệu dụng khoảng 859,2 mỗi nhánh. | Thiết kế nhắm chênh lệch 6 điểm phần trăm. Cần xác nhận đủ 40 người trước khi mở pilot. |

Các số trên là kết quả của nhóm. Đề xuất hiện tại là **No-go**. Bằng chứng tính toán nằm trong [bảng chi phí](bang_chi_phi.md) và [kế hoạch pilot](pilot_plan.yaml). Kết quả CP3 của hai thành viên sẽ được ghi trong [bảng lỗi](bang_loi.md) sau khi nhận phiếu độc lập của Quốc.

**Đối chiếu CP3.** [Phiếu xác nhận của Quốc](../../docs/CP3_phieu_PhamTranQuoc.md) ghi đủ 20 nhãn từ bảng tham khảo theo xác nhận của Quốc. Phiếu Dũng (commit `97505fa`) trùng 20/20 ca với bộ nhãn này. Bằng chứng đối chiếu theo mã nằm ở commit `9c02779`. Kiểm tra thư mục lab, các nhánh Git và stash chưa tìm thấy phiếu Quốc lập trước khi xem tham khảo. Tiêu chí độc lập chờ hướng dẫn của giảng viên. [Phần trình bày khi duyệt chéo](bang_loi.md#quốc-trình-bày-cp3-khi-duyệt-chéo) ghi cách tính, hai ví dụ phân loại và câu hỏi về phương án bổ sung. Năm ca đại diện trong [bảng lỗi](bang_loi.md) có cách phát hiện, hành động và vai trò phụ trách.

## 5. Công cụ AI đã dùng

Quốc phụ trách điều phối và bàn giao. Codex hỗ trợ soạn phiếu trắng, bản nháp hồ sơ và gợi ý tự đánh giá, phân tích tham khảo 20 ca, đối chiếu với phiếu Dũng, viết phần tính D1/E1 và chạy lại số liệu. Quốc đã rà lại hồ sơ và kiểm tra 20 nhãn ghi trên phiếu xác nhận.

## 6. Tự đánh giá

**Tự đánh giá đã được Quốc rà soát.** Phần điều phối có thể kiểm tra qua hai commit phân công và bàn giao. Nhóm đã nối kết quả A/B với quyết định pilot. Ở kịch bản xem lại toàn bộ và làm lại 15,3 phút, chi phí 12.415 đ/việc [simulated] vượt mốc nhân viên tự làm 12.000 đ. Vì vậy đề xuất hiện tại là No-go. Điểm cần cải thiện trong khâu điều phối là thu riêng hai phiếu gốc trước khi chia sẻ tài liệu tham khảo để nhóm đo được mức đồng thuận độc lập.

## Danh sách việc của Quốc

| Thời điểm | Việc cần làm | Trạng thái |
| --- | --- | --- |
| Trước CP3 | Đọc mục “Hai mươi ca lỗi” trong [đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và ghi riêng 20 nhãn trong 8 phút. | Có phiếu xác nhận từ nhãn tham khảo. Chưa có bộ nhãn độc lập của Quốc. |
| Khi cả hai gắn xong | Cùng Anh Dũng chép nguyên hai bộ vào [bảng lỗi](bang_loi.md), đếm ca trùng và tính tỉ lệ đồng thuận. Chốt nhãn cuối, giải thích mỗi ca bất đồng và chỉnh định nghĩa nếu đồng thuận dưới 80%. Chốt năm dòng khắc phục đủ năm loại với cách phát hiện đo được và vai trò phụ trách. | Quốc đã kiểm tra và xác nhận đủ 20 mã. Đã đối chiếu hai tài liệu, 20/20 mã trùng. Chưa có số đo đồng thuận độc lập. |
| Khi nhóm làm D và E | Cùng nhóm rà phương án pilot, chỉ số và hồ sơ launch. Dự duyệt chéo, chốt phiếu chấm và báo cáo nhóm từ kết quả thực tế. | Đã có dự thảo và số liệu D1/E1. A/B đã đối chiếu. Hồ sơ hiện đề xuất No-go và đang chờ kết quả duyệt chéo. |
| Khi có bằng chứng | Bổ sung email, đóng góp thực tế, tệp hoặc commit, cách Quốc tự kiểm tra phần dùng AI và tự đánh giá vào báo cáo này. Cập nhật đóng góp trong [TEAM.md](../../TEAM.md). | Đã điền email, dẫn chứng commit, khai báo công cụ và tự đánh giá. |
| Khi nhóm chốt bài | Rà danh sách tệp, xác nhận commit chốt và nộp link repo trên LMS bằng tài khoản cá nhân. | Đã kiểm đủ sáu tệp hồ sơ, báo cáo nhóm và bốn báo cáo cá nhân. Chương trình chạy hết, ba phép thử A1 đạt; YAML đọc được với bốn luật dừng. Mã bản chốt ghi trong [TEAM.md](../../TEAM.md). Quốc xác nhận đã nộp link repo trên LMS. |

Chi tiết từng checkpoint và yêu cầu nộp nằm trong [CHECKPOINTS.md](../../CHECKPOINTS.md) và [SUBMISSION.md](../../SUBMISSION.md).
