# Báo cáo cá nhân Lab 13 — Phạm Trấn Quốc

## 1. Thông tin thành viên

| Thông tin | Nội dung |
| --- | --- |
| Họ tên | Phạm Trấn Quốc |
| MSSV | 2A202604113 |
| Email | phamquoc896@gmail.com |
| Nhóm và lớp | Ghidorah, L3B |
| Vai trò | Trưởng nhóm và Người gắn nhãn 1 |

## 2. Phần việc phụ trách

Em phụ trách phân công, bàn giao tài liệu và rà hồ sơ Gate 2a trước khi nộp. Ở CP3, em phụ trách phiếu Người gắn nhãn 1 và cùng Trần Anh Dũng đối chiếu theo mã ca. Khi duyệt chéo, em tổng hợp câu hỏi của hai nhóm và ghi nhận phần đánh giá ToiYeuVinFast. Phân công chi tiết nằm trong [TEAM.md](../../TEAM.md).

## 3. Đóng góp cụ thể

### Điều phối, bàn giao và nộp bài

- Em công bố phân công đầu buổi và bàn giao phiếu trắng CP3, hướng dẫn từng người bắt đầu và dự thảo hồ sơ Gate 2a. Phong phụ trách code A/B, Quang Anh kiểm số và nhận code, Dũng gắn nhãn 2 và giữ hồ sơ. Hai mốc bàn giao là các commit `1c0c363` và `a94f634`.
- Em rà bộ tệp nộp gồm sáu tệp hồ sơ, báo cáo nhóm và bốn báo cáo cá nhân. Bản chạy của nhóm đã có kết quả A/B, D1 và E1. Em đã xác nhận nộp link repo trên LMS bằng tài khoản cá nhân. Mã commit của bản đã kiểm tra nằm trong [TEAM.md](../../TEAM.md).

### CP3 · Gắn nhãn độc lập và đối chiếu theo mã ca

Em tự gắn nhãn độc lập đủ các mã 01–20 ngay từ đầu trên [phiếu gắn nhãn của Quốc](../../docs/CP3_phieu_PhamTranQuoc.md) trước khi đối chiếu. Khi ghép theo mã với [phiếu độc lập của Dũng](../../docs/CP3_phieu_TranAnhDung.md), kết quả đạt **20/20 ca trùng (100% đồng thuận độc lập, ≥ 80%)**, gồm 4 ca do người dùng, 5 ca hệ thống, 4 ca ngữ cảnh, 4 ca giới hạn hệ thống và 3 ca ngầm, đồng thời khớp **20/20** với nhãn tham khảo. [Bảng đối chiếu CP3](bang_loi.md#đối-chiếu-hai-bộ-nhãn-độc-lập-theo-mã-ca-0120)

Bảng lỗi đã có năm biện pháp khắc phục. Hai ca dưới đây cho thấy cách dùng nguyên nhân gốc để chọn biện pháp:

| Ca và nhãn | Lý do phân loại | Cách phát hiện và xử lý |
| --- | --- | --- |
| 20 · Hệ thống | Hệ thống ghi hai khoản hoàn thành công cho cùng một giao dịch sau khi nhận lại yêu cầu. | Đếm bút toán theo mã khoản hoàn. Kỹ sư trưởng agent dùng lại khóa chống trùng khi gửi lại. Nếu phát hiện từ một ca, Giám đốc vận hành tắt trợ lý trong 30 phút kể từ lúc phát hiện. |
| 05 · Ngầm | Khoản hoàn tính trên giá trước giảm và sai lệch chỉ lộ khi kiểm tra mẫu. | Kế toán trưởng đối soát số tiền đã hoàn với phí thực trả, đưa khoản lệch vào hàng đợi để xử lý. |

### Rà đề xuất Gate 2a và duyệt chéo

Em ghi nhận năm câu hỏi Ghidorah và ToiYeuVinFast đã trao đổi, cùng đánh giá tổng quan **9/10** cho đội bạn. Phiếu lưu riêng phản hồi bằng văn bản của Ghidorah, mức **25/30 đề xuất** theo C6–C8 và quyết định hội đồng của Ghidorah dành cho ToiYeuVinFast là **Go có điều kiện**. [Phiếu duyệt chéo](phieu_cham.md)

Đề xuất của nhóm là **No-go ở thời điểm hiện tại**. Các số sau do nhóm tính và là căn cứ em dùng khi rà hồ sơ:

| Nội dung đã rà | Căn cứ và ý nghĩa |
| --- | --- |
| Chi phí và giới hạn chạy lại | A2 tính **4.472 đ/việc thành công [simulated]** từ 4.373.585 đ chia 978 việc. B3 cho thấy giới hạn 2 lần chạy có chi phí cả hệ thống thấp nhất trong ba phương án, khoảng **5.751 đ/yêu cầu [simulated]**, dù giới hạn 1 lần có chi phí trên mỗi việc thành công thấp hơn. |
| Rủi ro xem lại 100% | B4 cho **12.415 đ/việc thành công [simulated]** khi làm lại mất 15,3 phút. Bảng E1 bổ sung sự kiện đo phút xử lý thủ công để nhóm tính chi phí thực của cả hệ thống trên mỗi yêu cầu và so cùng đơn vị với mốc 12.000 đ/yêu cầu. |
| Cỡ mẫu và điều kiện an toàn | Thiết kế cần **20 người mỗi nhánh × 299 yêu cầu = 5.980 yêu cầu thô mỗi nhánh**. Chia cho hệ số thiết kế 6,96 còn khoảng **859,20 hiệu dụng**. Cần xác nhận đủ 40 người và duyệt từng bậc rollout theo điều kiện an toàn. |
| Chỉ số trong đợt chạy thử | Đạt chỉ số chính 994/1.200 (**82,83%**), sửa hoặc bỏ gợi ý 48/177 (**27,12%**) và mở lại 51/1.200 (**4,25%**). Đây là số quan sát từ đợt chạy thử chưa có đối chứng. |

Xem [bảng chi phí](bang_chi_phi.md), [kế hoạch pilot](pilot_plan.yaml), [bảng chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## 4. Bằng chứng

| Hạng mục | Bằng chứng để đối chiếu |
| --- | --- |
| Phân công và bàn giao | Commit `1c0c363` ghi phân công. Commit `a94f634` ghi bản bàn giao phiếu trắng và hồ sơ Gate 2a. |
| Rà nhãn CP3 | [Phiếu độc lập của em](../../docs/CP3_phieu_PhamTranQuoc.md), [phiếu độc lập của Dũng](../../docs/CP3_phieu_TranAnhDung.md) tại `97505fa` và bảng đối chiếu 20/20 trong [bảng lỗi](bang_loi.md). |
| Số liệu dùng khi rà | A/B của Phong tại `dc8e753`, phần kiểm số của Quang Anh tại `81a568d` và cập nhật hồ sơ của Dũng tại `0fc3bbe`. [Mã tính của nhóm](../../src/lab13.py) cho phép đối chiếu số liệu A/B, D1 và E1. |
| Duyệt chéo và nộp bài | [Năm câu hỏi trao đổi](phieu_cham.md#câu-hỏi-hai-nhóm-trao-đổi-khi-duyệt-chéo) và [bản hồ sơ đã kiểm tra](../../TEAM.md#thông-tin-nhóm). Việc nộp link trên LMS được ghi theo xác nhận của em. |

## 5. Công cụ AI đã dùng

Em phụ trách điều phối, bàn giao, gắn nhãn độc lập 20 ca CP3 và rà hồ sơ. Codex hỗ trợ trình bày phiếu, tổng hợp bảng đối chiếu, viết phần tính D1/E1 và chạy lại số liệu. Khi rà, em tự kiểm tra lại toàn bộ 20 ca đã gắn nhãn và đối chiếu số liệu A/B, D1, E1 về đúng tệp của nhóm.

## 6. Tự đánh giá

Điểm em làm được là giao việc rõ ràng, tự gắn nhãn độc lập CP3 đủ 20 ca trước khi đối chiếu với Dũng, để lại bằng chứng bàn giao và nối kết quả của từng phần với đề xuất Gate 2a. Ví dụ, chi phí ở B3 giúp chọn giới hạn chạy lại theo chi phí cả hệ thống, còn kịch bản B4 cho thấy cần đo lao động thực tế trước khi giảm xem lại hoặc mở rộng.

Điểm cần cải thiện là rà kỹ nội dung các bản nháp do AI hỗ trợ tổng hợp để tránh sai lệch giữa phần việc mình đã tự làm độc lập với phần đối chiếu tham khảo. Với hồ sơ hiện tại, em đã hoàn tất rà soát và đồng bộ toàn bộ hồ sơ nhóm theo đúng thực tế thực hiện.
