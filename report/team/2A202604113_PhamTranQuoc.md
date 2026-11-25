# Báo cáo cá nhân — Phạm Trấn Quốc

**Trạng thái:** Quốc đã phân công, bàn giao, rà hồ sơ, xác nhận 20 nhãn tham khảo và xác nhận đã nộp link trên LMS. A/B, D1 và E1 chạy được trên bản nhóm. Lượt bổ sung CP3 đang chờ giảng viên chấp thuận bộ ca hoặc phương án đánh giá thay thế.

## 1. Thông tin thành viên

- Họ tên: Phạm Trấn Quốc
- MSSV: 2A202604113
- Email: phamquoc896@gmail.com
- Nhóm: Ghidorah, lớp L3B
- Vai trò: Trưởng nhóm và Người gắn nhãn 1

## 2. Phần việc phụ trách

Theo dõi tiêu chí hoàn thành của các checkpoint. Ở CP3, tự gắn nhãn 20 ca theo nguyên nhân gốc và cùng Trần Anh Dũng đối chiếu sau khi cả hai đã hoàn tất bộ nhãn riêng. Phối hợp hoàn thiện bảng lỗi và tham gia các phần chung theo phân công trong [TEAM.md](../../TEAM.md).

## 3. Đóng góp cụ thể

| Việc                                            | Người phụ trách chính | Bằng chứng                                                                                                                                      |
| ----------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Công bố phân công và bàn giao tài liệu cho nhóm | Phạm Trấn Quốc        | Commit `1c0c363` cập nhật TEAM.md. Commit `a94f634` bàn giao phiếu trắng, phân công và bản nháp Gate 2a qua tài khoản Quoosc.                   |
| Bàn giao phiếu CP3 và tài liệu đối chiếu        | Phạm Trấn Quốc        | [Phiếu trắng](../../docs/CP3_phieu_gan_nhan_trang.md), [phần tham khảo CP3](bang_loi.md#phân-tích-tham-khảo). Phạm vi hỗ trợ được ghi ở mục 5.  |
| Điều phối rà cỡ mẫu, chỉ số và hồ sơ nhóm       | Phạm Trấn Quốc        | [Mã tính](../../src/lab13.py), [D1/D2](pilot_plan.yaml), [E1](chi_so.md). Phạm vi hỗ trợ được ghi ở mục 5.                                      |
| Rà hồ sơ và xác nhận 20 nhãn CP3 | Phạm Trấn Quốc | [Phiếu Quốc đã xác nhận](../../docs/CP3_phieu_PhamTranQuoc.md) và commit đối chiếu `9c02779`. |
| Chuẩn bị lượt bổ sung CP3 | Phạm Trấn Quốc | [Dự thảo tin nhắn xin bộ ca](../../docs/CP3_luot_bo_sung_tin_nhan.md) và [trạng thái lượt bổ sung](bang_loi.md#cp3--lượt-bổ-sung). |
| Ghi nhận nội dung duyệt chéo | Phạm Trấn Quốc | Đã cung cấp đánh giá tổng quan 9/10 cho ToiYeuVinFast và năm câu hỏi hai nhóm trao đổi. Xem [phiếu chấm](phieu_cham.md). |

## 4. Bằng chứng

Hai mốc bàn giao có thể kiểm tra bằng `git show --stat 1c0c363` và `git show --stat a94f634`. Sau bàn giao, Phong đưa A/B vào commit `dc8e753`, Quang Anh xác nhận đối chiếu ở `81a568d`, Dũng lưu phiếu riêng ở `97505fa` và cập nhật hồ sơ ở `0fc3bbe`.

**Căn cứ cho đề xuất của nhóm tại Gate 2a**

| Câu hỏi                                     | Kết quả có thể đối chiếu                                                                                                                       | Ý nghĩa cho quyết định                                                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Một việc thành công thực sự tốn bao nhiêu?  | Tổng 4.373.585 đ chia 978 việc thành công, xấp xỉ 4.472 đ/việc [simulated].                                                                    | Một yêu cầu thất bại vẫn tiêu token, gọi tool hoặc dùng giờ nhân viên. Những khoản đó vẫn vào tử số. Mẫu số đếm số việc đã giải quyết thành công. |
| Xem lại toàn bộ có còn tiết kiệm?           | Ở phạm vi nội địa và hàng nặng, B4 cho 11.743 đ/việc với giả định làm lại 9 phút và 12.415 đ/việc với 15,3 phút [simulated].                   | Kịch bản thứ hai vượt mốc nhân viên tự xử lý 12.000 đ. Pilot cần đo phút xem lại và làm lại thực tế.                                              |
| Cụm nhân viên ảnh hưởng thế nào đến cỡ mẫu? | Mỗi nhánh có 20 người × 299 yêu cầu = 5.980 yêu cầu. Hệ số thiết kế bằng 1 + (299 − 1) × 0,02 = 6,96. Cỡ mẫu hiệu dụng khoảng 859,2 mỗi nhánh. | Thiết kế nhắm chênh lệch 6 điểm phần trăm. Cần xác nhận đủ 40 người trước khi mở pilot.                                                           |

Các số trên là kết quả của nhóm. Đề xuất hiện tại là **No-go**. Bằng chứng tính toán nằm trong [bảng chi phí](bang_chi_phi.md) và [kế hoạch pilot](pilot_plan.yaml). Kết quả CP3 của hai thành viên sẽ được ghi trong [bảng lỗi](bang_loi.md) sau khi nhận phiếu độc lập của Quốc.

**Đối chiếu tham khảo CP3.** Quốc đã rà và xác nhận [20 nhãn tham khảo](../../docs/CP3_phieu_PhamTranQuoc.md). Kết quả đối chiếu với phiếu gốc của Dũng (commit `97505fa`) là 20/20, lưu tại `9c02779`. Đồng thuận độc lập đang chờ lượt bổ sung. [Bảng lỗi](bang_loi.md) có năm ca đại diện kèm tín hiệu phát hiện, hành động và vai trò phụ trách.

### CP3 – Lượt bổ sung

**Trạng thái: Đang chờ hướng dẫn của giảng viên.** Chưa có bộ ca mới nào được chấp thuận trong repo, nên chưa lập hai phiếu trắng và chưa có bảng đối chiếu cho lượt bổ sung. Hai phiếu cũ và kết quả 20/20 trong mục “Đối chiếu tham khảo” được giữ nguyên.

| Hạng mục                                   | Đường dẫn                                                                    | Trạng thái                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------- |
| Tin nhắn xin bộ ca hoặc phương án thay thế | [docs/CP3_luot_bo_sung_tin_nhan.md](../../docs/CP3_luot_bo_sung_tin_nhan.md) | Đã soạn, chờ gửi giảng viên                 |
| Phiếu của Quốc                             | `docs/CP3_bo_sung_phieu_PhamTranQuoc.md`                                     | Chưa tạo — chờ bộ ca được duyệt             |
| Phiếu của Dũng                             | `docs/CP3_bo_sung_phieu_TranAnhDung.md`                                      | Chưa tạo — chờ bộ ca được duyệt             |
| Bảng đối chiếu                             | [bang_loi.md#cp3--lượt-bổ-sung](bang_loi.md#cp3--lượt-bổ-sung)               | Chưa có dữ liệu — chờ cả hai phiếu hoàn tất |

Số ca hợp lệ, số ca trùng, tỉ lệ đồng thuận và danh sách ca còn chờ hai người chốt chưa xác định vì chưa có bộ ca. Mức khớp đáp án giảng viên chỉ được tính khi có đáp án chính thức; kết quả 20/20 ở mục tham khảo không phải đáp án chính thức.

## 5. Công cụ AI đã dùng

Quốc phụ trách chính việc điều phối, bàn giao và rà hồ sơ. Quốc đã kiểm đủ 20 mã, xác nhận các nhãn trên phiếu tham khảo và rà lại phần tự đánh giá. Codex hỗ trợ soạn phiếu và dự thảo, đề xuất nhãn tham khảo, đối chiếu tài liệu, viết phần tính D1/E1, chạy lại số liệu và chuẩn bị câu hỏi xin hướng dẫn bổ sung CP3.

## 6. Tự đánh giá

**Tự đánh giá đã được Quốc rà soát.** Hai commit phân công và bàn giao ghi nhận phần điều phối. Kịch bản xem lại toàn bộ với 15,3 phút làm lại có chi phí 12.415 đ/việc thành công [simulated], cao hơn mốc tham chiếu 12.000 đ. Đây là lý do cần đo chi phí thực trên cùng đơn vị trước khi đề xuất mở rộng. Điểm cần cải thiện là thu riêng hai phiếu gốc trước khi chia sẻ tài liệu tham khảo. Lượt bổ sung CP3 chờ hướng dẫn của giảng viên.

## Danh sách việc của Quốc

| Thời điểm            | Việc cần làm                                                                                                                                                                                                                                                                      | Trạng thái                                                                                                                                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trước CP3            | Đọc mục “Hai mươi ca lỗi” trong [đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và ghi riêng 20 nhãn trong 8 phút.                                                                                                                                                         | Chưa có bộ nhãn của Quốc trong repo.                                                                                                                                                                                                |
| Khi có bộ ca bổ sung | Nhận bộ ca mới được giảng viên chấp thuận; lập hai phiếu trắng giống nhau cho Quốc và Dũng; gắn nhãn độc lập; chỉ đối chiếu khi cả hai đã gửi bản hoàn tất.                                                                                                                       | Đang chờ hướng dẫn. Đã soạn [tin nhắn xin bộ ca](../../docs/CP3_luot_bo_sung_tin_nhan.md).                                                                                                                                          |
| Khi cả hai gắn xong  | Cùng Anh Dũng chép nguyên hai bộ vào [bảng lỗi](bang_loi.md), đếm ca trùng và tính tỉ lệ đồng thuận. Chốt nhãn cuối, giải thích mỗi ca bất đồng và chỉnh định nghĩa nếu đồng thuận dưới 80%. Chốt năm dòng khắc phục đủ năm loại với cách phát hiện đo được và vai trò phụ trách. | Đã có phần tham khảo và phiếu riêng của Dũng. Còn chờ phiếu độc lập của Quốc và kết quả đối chiếu.                                                                                                                                  |
| Khi nhóm làm D và E  | Cùng nhóm rà phương án pilot, chỉ số và hồ sơ launch. Dự duyệt chéo, chốt phiếu chấm và báo cáo nhóm từ kết quả thực tế.                                                                                                                                                          | Đã có dự thảo và số liệu D1/E1. A/B đã đối chiếu. Hồ sơ hiện đề xuất No-go và đang chờ kết quả duyệt chéo.                                                                                                                          |
| Khi có bằng chứng    | Bổ sung email, đóng góp thực tế, tệp hoặc commit, cách Quốc tự kiểm tra phần dùng AI và tự đánh giá vào báo cáo này. Cập nhật đóng góp trong [TEAM.md](../../TEAM.md).                                                                                                            | Đã điền email, dẫn chứng commit, khai báo công cụ và tự đánh giá.                                                                                                                                                                   |
| Khi nhóm chốt bài    | Rà danh sách tệp, xác nhận commit chốt và nộp link repo trên LMS bằng tài khoản cá nhân.                                                                                                                                                                                          | Đã kiểm đủ sáu tệp hồ sơ, báo cáo nhóm và bốn báo cáo cá nhân. Chương trình chạy hết, ba phép thử A1 đạt; YAML đọc được với bốn luật dừng. Mã bản chốt ghi trong [TEAM.md](../../TEAM.md). Quốc xác nhận đã nộp link repo trên LMS. |

Chi tiết từng checkpoint và yêu cầu nộp nằm trong [CHECKPOINTS.md](../../CHECKPOINTS.md) và [SUBMISSION.md](../../SUBMISSION.md).
