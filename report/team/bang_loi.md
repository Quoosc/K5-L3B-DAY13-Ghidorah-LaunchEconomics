# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Trấn Quốc · Người gắn nhãn 2: Trần Anh Dũng

Mỗi người lập bộ 20 nhãn riêng trong 8 phút, giữ riêng cho đến khi cả hai đã hoàn tất. Sau đó chép nguyên hai bộ vào bảng. Mọi thay đổi sau khi thảo luận được ghi ở cột “Nhãn thống nhất”.

**Nhận phiếu:** Chờ hai bộ nhãn gốc. Dùng [phiếu trắng CP3](../../docs/CP3_phieu_gan_nhan_trang.md) khi làm riêng. Trước khi nhập, kiểm đủ mã 01–20 đúng một lần cho mỗi người và kiểm nhãn thuộc năm loại trên.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

**Mã ca bất đồng:** Chờ hai bộ nhãn gốc.

**Tỉ lệ khớp đáp án giảng viên:** Chờ đáp án chính thức và nhãn thống nhất.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |

## Rà soát trước khi chốt CP3

- [ ] Hai bộ nhãn gốc có đủ ca 1–20 và được giữ nguyên sau khi đối chiếu.
- [ ] Cột “Trùng?” so hai bộ nhãn gốc. Tỉ lệ đồng thuận từ 80% khi có ít nhất 16 ca trùng. Nếu thấp hơn, ghi định nghĩa đã chỉnh ở mục quy tắc phân biệt.
- [ ] Cột “Nhãn thống nhất” có đủ 20 ca. Mỗi ca bất đồng có một câu giải thích cách phân biệt.
- [ ] Năm ca khắc phục đại diện cho đủ năm loại theo nhãn đã thống nhất. Mỗi dòng có dấu hiệu đo được, cách xử lý và một vai trò chịu trách nhiệm.
- [ ] Khi có đáp án của giảng viên, đối chiếu nhãn thống nhất với đáp án theo ngưỡng 16/20 của rubric. Đây là phép kiểm tra riêng với tỉ lệ đồng thuận của hai người.

## Phân tích tham khảo của Codex

Chỉ mở sau khi cả hai đã ghi xong bộ nhãn độc lập. Codex đối chiếu tình huống trong đề với [nhãn tham khảo trong hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Các nhãn dưới đây phục vụ thảo luận và rà soát sau khi gắn nhãn. Cột nhãn gốc và tỉ lệ đồng thuận sử dụng kết quả thực tế của hai thành viên.

<details>
<summary>Xem 20 nhãn tham khảo và năm đề xuất khắc phục</summary>

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

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Vai trò phụ trách đề xuất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Đếm sự kiện `refund_destination_invalid` theo ngày và rà mỗi ca lệnh đã gửi nhưng bị ngân hàng từ chối vì định dạng tài khoản. | Kiểm tra định dạng theo ngân hàng trước khi gửi lệnh và yêu cầu khách sửa thông tin. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát hằng ngày và cảnh báo khi cùng mã giao dịch hoàn nghiệp vụ có từ hai bút toán hoàn thành công. | Dùng cùng khóa chống trùng cho các lần gửi lại của một giao dịch và trả trạng thái lệnh hiện có. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Đếm mỗi ngày số thông báo hoàn tiền gửi trong khung giờ yên tĩnh theo giờ địa phương của khách. | Xếp thông báo vào hàng đợi và gửi khi hết khung giờ yên tĩnh. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Theo dõi hằng tuần số sự kiện `unsupported_input` có kiểu đầu vào là âm thanh và số ca khách gửi lại bằng văn bản. | Báo rõ kênh chưa xử lý giọng nói và hướng dẫn gửi văn bản hoặc chuyển nhân viên. | PM trợ lý hoàn phí |
| 5 | Ngầm | Đối soát hằng tuần số đơn có mã giảm giá mà khoản hoàn vượt số tính theo phí thực trả. | Tính trên khoản phí đủ điều kiện sau giảm giá và đưa giao dịch chênh lệch vào hàng đợi đối soát. | Kế toán trưởng |

</details>
