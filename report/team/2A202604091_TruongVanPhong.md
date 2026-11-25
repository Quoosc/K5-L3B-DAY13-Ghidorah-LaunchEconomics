# Báo cáo cá nhân — Trương Văn Phong - 2A202604091

## 1. Thông tin thành viên

- Họ tên: Trương Văn Phong
- MSSV: 2A202604091
- Email: 26ai.phongtv@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code nửa đầu buổi, phụ trách nhiệm vụ A và B

## 2. Phần việc phụ trách

- Cài và chạy chương trình trong `src/`, kiểm tra môi trường `pandas`, `statsmodels`.
- Hoàn thiện A1, A2, A3, A4 và B1, B2, B3, B4 trong `src/lab13.py`.
- Chạy lại chương trình, đối chiếu kết quả và điền phần A, B trong `report/team/bang_chi_phi.md`.
- Bàn giao `src/lab13.py` cho Nguyễn Quốc Quang Anh sau giải lao để tiếp tục phần D1.

## 3. Đóng góp cụ thể

- Viết ba hàm A1: `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước đều đạt 1,20 · 1,25 · 1,25.
- Viết `mo_hinh(runs, reqs, ...)`: cộng token và tool trên mọi lần chạy, cộng giờ xem lại và làm lại theo cột `_simulated`, chia cho số việc thành công; hỗ trợ các tham số giá, hệ số và `max_lan_chay` cho nhiệm vụ B.
- Viết các khối in A2, A3, A4, B1, B2, B3, B4 trong `lab13.py`; phần A3 có thêm tỉ lệ run ok theo từng lần thử để trả lời câu hỏi chạy lại có giúp không.
- Điền đầy đủ `report/team/bang_chi_phi.md`: A1, A2, A3, A4, B1, B2, B3, B4; mọi số lấy từ cột `_simulated` đều có nhãn `simulated`.
- Đối chiếu kết quả với số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; các bảng A2, A3, A4 và B1 khớp trong sai số 2%.

## 4. Bằng chứng

- File đã thực hiện: `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Lệnh chạy: `cd src` rồi `.\.venv\Scripts\python.exe lab13.py`.
- Kết quả A1: `Ba phép thử đáp án biết trước: ĐẠT`.
- Kết quả A2: token 245.585 đ; tool 84.000 đ; xem lại 1.780.000 đ [simulated]; làm lại 2.264.000 đ [simulated]; tổng 4.373.585 đ; 978 việc thành công; 4.472 đ/việc [simulated]; hoá đơn token + tool 274,7 đ/yêu cầu; gấp 16,3 lần.
- Kết quả A3: `quoc_te` có chi phí 22.515 đ/việc [simulated], bằng 1,88× so với 12.000 đ và chỉ 27,3% thành công; tỉ lệ run ok giảm 30,0% → 11,4% → 2,2% qua ba lần thử.
- Kết quả A4: 45.000 yêu cầu/tháng cho 33.750 việc thành công; chi phí cố định 1.185 đ/việc; tổng 4.599 đ = 0,38× [simulated]; giảm nửa khối lượng là 5.784 đ = 0,48× [simulated].
- Kết quả B1: làm lại gấp đôi làm chi phí tăng +51,8%; xem lại gấp đôi +40,7%; lương tăng 25% +23,1%; token gấp đôi chỉ +5,6%.
- Kết quả B3: giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ [simulated]); giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ [simulated]).
- Kết quả B4: xem lại 100% cho 11.743 đ = 0,98× [simulated]; với 15,3 phút làm lại theo dữ liệu giả lập là 12.415 đ = 1,03× [simulated].
- Tự kiểm tra bằng phép tính tay: 890 phút xem lại × 2.000 đ/phút = 1.780.000 đ; tổng 245.585 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585 đ.
- Phần code và bảng A/B đã được đưa vào nhánh main tại commit `dc8e753`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI trong OpenCode để gợi ý cấu trúc các hàm A1, `mo_hinh`, cách lọc `max_lan_chay`, cách tính chi phí cả hệ thống ở B3 và cách trình bày bảng B4.
- Tự kiểm tra lại bằng cách chạy `python lab13.py`, đọc kết quả từng bảng, đối chiếu với số tham chiếu trong `docs/`, kiểm tra tổng các khoản bằng tổng chi phí và tính tay 890 × 2.000 = 1.780.000 đ.
- Không dùng AI để tạo nhãn lỗi hay kết quả duyệt chéo; phần C và phiếu chấm do các thành viên khác thực hiện theo đúng quy định.

## 6. Tự đánh giá

- Hoàn thành đúng phần được phân công: A1–A4 và B1–B4 trong code, cùng bảng A/B trong hồ sơ.
- Code chạy được từ đầu đến cuối, ba phép thử A1 đạt, các số chính khớp tham chiếu.
- Phần D1 được để lại đúng chỗ `TODO CP4` để bàn giao cho Quang Anh; phần C, D, E còn lại do nhóm phối hợp hoàn thiện.
- Cần cải thiện thêm cách trình bày bảng trên console và bổ sung kiểm tra tự động cho các tổng chi phí nếu có thời gian.
