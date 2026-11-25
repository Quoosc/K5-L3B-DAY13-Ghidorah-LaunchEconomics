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

### CP3 · Rà nhãn và đối chiếu theo mã ca

Em kiểm đủ các mã 01–20 và xác nhận 20 nhãn từ bảng tham khảo. Khi ghép theo mã với phiếu gốc của Dũng, có **20/20 ca trùng**, gồm 4 ca do người dùng, 5 ca hệ thống, 4 ca ngữ cảnh, 4 ca giới hạn hệ thống và 3 ca ngầm. Kết quả này đo mức khớp giữa hai tài liệu. Phiếu của em được xác nhận sau khi xem tham khảo, nên bằng chứng đồng thuận độc lập vẫn cần bổ sung. [Bảng đối chiếu CP3](bang_loi.md#đối-chiếu-tham-khảo-theo-mã-ca-0120)

Bảng lỗi đã có năm biện pháp khắc phục. Hai ca dưới đây cho thấy cách dùng nguyên nhân gốc để chọn biện pháp:

| Ca và nhãn | Lý do phân loại | Cách phát hiện và xử lý |
| --- | --- | --- |
| 20 · Hệ thống | Hệ thống ghi hai khoản hoàn thành công cho cùng một giao dịch sau khi nhận lại yêu cầu. | Đếm bút toán theo mã khoản hoàn. Kỹ sư trưởng agent dùng lại khóa chống trùng khi gửi lại. Nếu phát hiện từ một ca, Giám đốc vận hành tắt trợ lý trong 30 phút kể từ lúc phát hiện. |
| 05 · Ngầm | Khoản hoàn tính trên giá trước giảm và sai lệch chỉ lộ khi kiểm tra mẫu. | Kế toán trưởng đối soát số tiền đã hoàn với phí thực trả, đưa khoản lệch vào hàng đợi để xử lý. |

### Rà đề xuất Gate 2a và duyệt chéo

Em ghi nhận năm câu hỏi Ghidorah và ToiYeuVinFast đã trao đổi, cùng đánh giá tổng quan **9/10** cho đội bạn. Phiếu lưu riêng phản hồi bằng văn bản của Ghidorah và mức **25/30 đề xuất** theo C6–C8. Điểm chính thức và quyết định của hội đồng chưa được ghi nhận. [Phiếu duyệt chéo](phieu_cham.md)

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
| Rà nhãn CP3 | [Phiếu em đã xác nhận](../../docs/CP3_phieu_PhamTranQuoc.md), [phiếu gốc của Dũng](../../docs/CP3_phieu_TranAnhDung.md) tại `97505fa` và kết quả ghép theo mã tại `9c02779`. |
| Số liệu dùng khi rà | A/B của Phong tại `dc8e753`, phần kiểm số của Quang Anh tại `81a568d` và cập nhật hồ sơ của Dũng tại `0fc3bbe`. [Mã tính của nhóm](../../src/lab13.py) cho phép đối chiếu số liệu A/B, D1 và E1. |
| Duyệt chéo và nộp bài | [Năm câu hỏi trao đổi](phieu_cham.md#câu-hỏi-hai-nhóm-trao-đổi-khi-duyệt-chéo) và [bản hồ sơ đã kiểm tra](../../TEAM.md#thông-tin-nhóm). Việc nộp link trên LMS được ghi theo xác nhận của em. |

### CP3 – Gắn nhãn độc lập (lượt bổ sung)

Theo [rubric C3](../../RUBRIC.md#rubric), bảng đã có đủ năm loại lỗi, mỗi loại có tín hiệu phát hiện đo được và một vai trò phụ trách. Hồ sơ còn thiếu kết quả so **hai bộ nhãn độc lập** (ngưỡng đồng thuận 80%) và kết quả so với **đáp án chính thức** (ngưỡng 16/20). Đã chuẩn bị [tin nhắn xin hướng dẫn](../../docs/CP3_luot_bo_sung_tin_nhan.md). Nếu giảng viên duyệt bộ ca mới, em và Dũng sẽ lưu hai phiếu riêng, tính tỉ lệ đồng thuận trước khi trao đổi và ghi kết quả ở [mục lượt bổ sung](bang_loi.md#cp3--gắn-nhãn-độc-lập-lượt-bổ-sung).

## 5. Công cụ AI đã dùng

Em phụ trách điều phối, bàn giao và rà hồ sơ. Em đã kiểm đủ 20 mã, rà nội dung phiếu và xác nhận các nhãn tham khảo. Codex hỗ trợ soạn phiếu và dự thảo báo cáo, đề xuất nhãn tham khảo, đối chiếu tài liệu, viết phần tính D1/E1 và chạy lại số liệu. Khi rà, em dùng phiếu và bảng đối chiếu theo mã để kiểm tra phạm vi 20 ca, đồng thời dẫn số liệu A/B, D1 và E1 về đúng tệp của nhóm. [Phiếu luyện tập](../../docs/CP3_phieu_luyen_tap_20_ca_moi.md) lưu riêng để ôn cách phân loại.

## 6. Tự đánh giá

Điểm em làm được là giao việc rõ ràng, để lại bằng chứng bàn giao và nối kết quả của từng phần với đề xuất Gate 2a. Ví dụ, chi phí ở B3 giúp chọn giới hạn chạy lại theo chi phí cả hệ thống, còn kịch bản B4 cho thấy cần đo lao động thực tế trước khi giảm xem lại hoặc mở rộng.

Điểm cần cải thiện là cách thu bằng chứng CP3. Lần sau em sẽ thu và lưu riêng hai phiếu gốc trước khi chia sẻ tài liệu tham khảo, sau đó ghi tỉ lệ đồng thuận ban đầu và các ca cần thảo luận. Với hồ sơ hiện tại, em đã rà soát và xác nhận 20 nhãn tham khảo. Việc bổ sung bằng chứng độc lập theo C3 đang chờ hướng dẫn của giảng viên.
