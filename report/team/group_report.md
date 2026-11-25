# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Ghidorah
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí, mức sử dụng và rủi ro của trợ lý hoàn phí LogiX-VN để đề xuất một pilot có đối chứng. Dữ liệu chạy thử gồm 1.200 yêu cầu giả lập.

## 3. Giải pháp

- A/B dùng trace và dữ liệu yêu cầu để tính chi phí, so với nhân viên tự làm và phân tích độ nhạy. Kết quả đã được đối chiếu với code chạy trên hai CSV. Chi tiết ở [bảng chi phí](bang_chi_phi.md).
- **CP3.** Quốc và Dũng tự gắn nhãn độc lập đủ 20 ca trước khi đối chiếu. Hai phiếu gốc trùng **20/20 ca (100% đồng thuận độc lập)** và khớp 20/20 nhãn tham khảo. Bảng lỗi có năm phương án khắc phục đủ năm loại. Xem [bảng lỗi](bang_loi.md).
- D đề xuất ngẫu nhiên theo nhân viên với đối chứng chạy cùng thời gian. Xem [kế hoạch pilot](pilot_plan.yaml).
- E tính chỉ số từ CSV và thiết kế sự kiện để đo trong pilot. Xem [chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Chi phí mỗi việc thành công là 4.472 đ [simulated]. Giới hạn 2 lần chạy cho chi phí cả hệ thống khoảng 5.751 đ/yêu cầu [simulated], so với mốc 12.000 đ tự làm. Làm lại gấp đôi làm chi phí mỗi việc thành công tăng 51,8% [simulated].

Đợt thử có 994/1.200 yêu cầu đạt chỉ số chính (82,83%), 48/177 yêu cầu được xem lại có sửa hoặc bỏ gợi ý (27,12%) và 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%). B4 cho 12.415 đ/việc thành công [simulated] nếu làm lại mất 15,3 phút. Để quyết định giảm xem lại, cần đo chi phí cả hệ thống theo đ/yêu cầu và kiểm tra an toàn. Đề xuất hiện tại là No-go.

Ghidorah và ToiYeuVinFast đã trao đổi năm câu hỏi về lịch pilot, điều kiện giảm xem lại, luật dừng khi hoàn trùng, tính độc lập của CP3 và cách xử lý kết quả chưa rõ. Quốc ghi đánh giá tổng quan 9/10 cho ToiYeuVinFast, mức đề xuất C6–C8 lần lượt 10, 10 và 5 điểm (**25/30**) và quyết định hội đồng của Ghidorah là **Go có điều kiện**. [Phiếu chấm](phieu_cham.md#câu-hỏi-hai-nhóm-trao-đổi-khi-duyệt-chéo) lưu cả câu hỏi đã trao đổi và phản hồi bằng văn bản sau khi rà hồ sơ.

## 5. Khó khăn và cách xử lý

Mẫu lịch sử có 20 nhân viên tại 6 depot. Trước khi trình pilot, Giám đốc vận hành cần xác nhận 40 nhân viên đủ điều kiện, danh sách phân nhánh và dự báo đủ 299 yêu cầu mỗi người. Nếu chỉ có 20 người, chia 10+10 có trần dưới 500 yêu cầu hiệu dụng mỗi nhánh, thấp hơn 859. Giữ No-go cho thiết kế hiện tại, tiếp tục xử lý thủ công và tuyển thêm người hoặc trình lại thiết kế có đối chứng.

Hai bậc 10% và 25% thu yêu cầu trong 7 ngày rồi chờ đủ theo dõi an toàn. Ở bậc 50%, hết tuần chỉ kiểm tiến độ tuyển. Nếu thiếu mẫu, giữ nguyên hai nhánh và thu tiếp trong giới hạn đã chốt trước. Ngày quyết định tính từ ngày khóa mẫu thực tế, khi đã đủ 8 ngày theo dõi và hoàn tất rà an toàn. Một ca hoàn trùng kích hoạt tắt trợ lý trong 30 phút kể từ lúc phát hiện.

## 6. Tổng hợp đóng góp

Quốc điều phối, kiểm tra hồ sơ và gắn nhãn độc lập 20 ca CP3. Phong triển khai A/B, Quang Anh kiểm số và đối chiếu D1/E1, Dũng gắn nhãn độc lập và giữ hồ sơ launch. Xem [phân công và bằng chứng của từng người](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Chạy thử thiếu đối chứng nên chỉ số quan sát chưa cho biết tác động của trợ lý. Phương án ngẫu nhiên theo nhân viên cần 299 yêu cầu mỗi người và đủ 20 người mỗi nhánh để nhận biết chênh lệch 6 điểm theo giả định của đề.

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx)
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- [Rubric](../../RUBRIC.md)
