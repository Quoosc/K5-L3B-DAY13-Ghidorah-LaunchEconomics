# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Đối chiếu tham khảo theo mã ca 01–20

Phạm Trấn Quốc đã rà soát và xác nhận các nhãn dựa trên bảng tham khảo. Bảng dưới ghép [phiếu Quốc xác nhận](../../docs/CP3_phieu_PhamTranQuoc.md) với [phiếu gốc của Dũng](../../docs/CP3_phieu_TranAnhDung.md) theo mã 01–20.

| Ca | Quốc xác nhận sau rà soát | Dũng ghi trên phiếu gốc | Kết quả đối chiếu |
| --: | --- | --- | --- |
| 01 | Do người dùng | Do người dùng | Trùng |
| 02 | Hệ thống | Hệ thống | Trùng |
| 03 | Ngữ cảnh | Ngữ cảnh | Trùng |
| 04 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng |
| 05 | Ngầm | Ngầm | Trùng |
| 06 | Do người dùng | Do người dùng | Trùng |
| 07 | Hệ thống | Hệ thống | Trùng |
| 08 | Hệ thống | Hệ thống | Trùng |
| 09 | Do người dùng | Do người dùng | Trùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Trùng |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng |
| 12 | Ngầm | Ngầm | Trùng |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng |
| 14 | Do người dùng | Do người dùng | Trùng |
| 15 | Hệ thống | Hệ thống | Trùng |
| 16 | Ngữ cảnh | Ngữ cảnh | Trùng |
| 17 | Ngầm | Ngầm | Trùng |
| 18 | Ngữ cảnh | Ngữ cảnh | Trùng |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng |
| 20 | Hệ thống | Hệ thống | Trùng |

**Hai phiếu khớp 20/20 ca (100%).** Không có mã ca khác nhãn cần giải thích trong lần đối chiếu này. Phiếu Quốc xác nhận dùng nhãn tham khảo. Để tính đồng thuận độc lập cần bộ nhãn Quốc lập trước khi xem tham khảo. Chưa có kết quả đối chiếu với đáp án chính thức của giảng viên.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Năm biện pháp đề xuất từ các tình huống trong đề, để nhóm xem xét khi chốt CP3 và chuẩn bị pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Vai trò phụ trách đề xuất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Đếm sự kiện `refund_destination_invalid` theo ngày và rà mỗi ca lệnh đã gửi nhưng bị ngân hàng từ chối vì định dạng tài khoản. | Kiểm tra định dạng theo ngân hàng trước khi gửi lệnh và yêu cầu khách sửa thông tin. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát hằng ngày và cảnh báo khi cùng mã giao dịch hoàn nghiệp vụ có từ hai bút toán hoàn thành công. | Dùng cùng khóa chống trùng cho các lần gửi lại của một giao dịch và trả trạng thái lệnh hiện có. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Đếm mỗi ngày số thông báo hoàn tiền gửi trong khung giờ yên tĩnh theo giờ địa phương của khách. | Xếp thông báo vào hàng đợi và gửi khi hết khung giờ yên tĩnh. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Theo dõi hằng tuần số sự kiện `unsupported_input` có kiểu đầu vào là âm thanh và số ca khách gửi lại bằng văn bản. | Báo rõ kênh chưa xử lý giọng nói và hướng dẫn gửi văn bản hoặc chuyển nhân viên. | PM trợ lý hoàn phí |
| 5 | Ngầm | Đối soát hằng tuần số đơn có mã giảm giá mà khoản hoàn vượt số tính theo phí thực trả. | Tính trên khoản phí đủ điều kiện sau giảm giá và đưa giao dịch chênh lệch vào hàng đợi đối soát. | Kế toán trưởng |

## Rà soát trước khi chốt CP3

- [ ] Hai bộ nhãn gốc có đủ ca 1–20 và được giữ nguyên sau khi đối chiếu.
- [ ] Cột “Trùng?” so hai bộ nhãn gốc. Tỉ lệ đồng thuận từ 80% khi có ít nhất 16 ca trùng. Nếu thấp hơn, ghi định nghĩa đã chỉnh ở mục quy tắc phân biệt.
- [ ] Cột “Nhãn thống nhất” có đủ 20 ca. Mỗi ca bất đồng có một câu giải thích cách phân biệt.
- [ ] Năm ca khắc phục đại diện cho đủ năm loại theo nhãn đã thống nhất. Mỗi dòng có dấu hiệu đo được, cách xử lý và một vai trò chịu trách nhiệm.
- [ ] Khi có đáp án của giảng viên, đối chiếu nhãn thống nhất với đáp án theo ngưỡng 16/20 của rubric. Đây là phép kiểm tra riêng với tỉ lệ đồng thuận của hai người.

## Phân tích tham khảo

Xem [bảng đối chiếu tham khảo](../../docs/CP3_doi_chieu_tham_khao.md) để xem kết quả so sánh từng ca với phiếu Dũng.

Chỉ mở sau khi cả hai đã ghi xong bộ nhãn độc lập. Phần này dựa trên tình huống trong đề và [nhãn tham khảo trong hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Cột nhãn gốc và tỉ lệ đồng thuận sử dụng kết quả thực tế của hai thành viên.

<details>
<summary>Xem 20 nhãn tham khảo và kết quả đối chiếu với phiếu Dũng</summary>

Đối chiếu theo mã ca giữa phiếu Dũng (commit `97505fa`) và bảng tham khảo cho kết quả 20/20 ca trùng (100%). Tỉ lệ đồng thuận giữa Quốc và Dũng đang chờ phiếu riêng của Quốc.

| Ca | Nhãn tham khảo | Lý do |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số tài khoản. |
| 2 | Hệ thống | Trợ lý truyền loại hàng thường cho kiện hàng nặng, dẫn đến hoàn thiếu. |
| 3 | Ngữ cảnh | Tiền về ví theo thiết kế, còn khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu về chặng do hãng nước ngoài giao. |
| 5 | Ngầm | Hoàn theo giá trước giảm và chỉ phát hiện khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn luồng giao trễ cho yêu cầu về hàng vỡ. |
| 7 | Hệ thống | Trợ lý báo thành công dù sổ cái chưa xác nhận giao dịch. |
| 8 | Hệ thống | Trợ lý dẫn một điều khoản không có trong chính sách hiện hành. |
| 9 | Do người dùng | Khách đưa mã đơn sàn thay vì mã vận đơn. |
| 10 | Ngữ cảnh | Quyết định đúng điều khoản bất khả kháng, trong khi ứng dụng vẫn tạo kỳ vọng giao trong 24 giờ. |
| 11 | Giới hạn hệ thống | Trợ lý chưa hỗ trợ xử lý âm thanh. |
| 12 | Ngầm | Kết quả đúng, nhưng chi phí token bất thường kéo dài mà chưa được phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm đối tác nằm ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm xác nhận đã nhận tiền trước khi thực nhận. |
| 15 | Hệ thống | Tính sai tỉ lệ hoàn theo chính sách và bị phát hiện khi nhân viên xem lại. |
| 16 | Ngữ cảnh | Gửi ngay đúng thiết kế nhưng thời điểm gửi gây phiền cho khách. |
| 17 | Ngầm | Bảng giá lưu trong bộ nhớ đệm đã cũ, khoản lệch nhỏ kéo dài và không có ca mở lại. |
| 18 | Ngữ cảnh | Số tiền đúng, nhưng thông báo thiếu cách tính nên khách hiểu khác. |
| 19 | Giới hạn hệ thống | Đơn nằm ngoài thời hạn dữ liệu mà trợ lý truy cập được. |
| 20 | Hệ thống | Thiếu cơ chế chống trùng nên cùng một khoản được hoàn hai lần. |

</details>
