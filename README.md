# grade_the_exams
phân tích và tính toán điểm thi
## Cách cài đặt.
1. Cài đặt môi trường.
Để có thể sử dụng công cụ, bạn cần cài đặt python và thư viện pandas. Mở terminal của bạn và sử dụng các câu lệnh đầu cuối sau:
        pip install pandas
2. Cách sử dụng.
2.1. Chuẩn bị dữ liệu
  Đặt file "hoang_tri_grade_the_exams.py" cùng thư mục với các file dữ liệu cần xử lý của bạn
  Giải nén file " Data Files " để lấy dữ liệu 
2.2 
File dữ liệu của bạn phải là file text. Mỗi file dữ liệu chứa một loạt câu trả lời của học sinh ở định dạng sau:
  "N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
hoặc:
  "N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,"
- Giá trị đầu tiên là số ID của sinh viên. 25 chữ cái sau là câu trả lời của học sinh cho kỳ thi. Tất cả các giá trị được phân tách bằng dấu phẩy. Nếu không có chữ cái nào sau dấu phẩy, điều này có nghĩa là học sinh đã bỏ qua việc trả lời câu hỏi.
Lưu ý rằng các dòng dữ liệu phải đúng với quy chuẩn được đề cập phía trên, các dữ liệu không đạt chuẩn ví dụ như:
- Không có đủ câu trả lời:
  "N12345678,B,A,D,D,C,B"
- Có quá nhiều câu trả lời:
  "N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E"
ID sinh viên N# không đạt chuẩn(N# phải chứa ký tự “N” theo sau là 8 ký tự số).
Các dòng dữ liệu không đạt chuẩn sẽ xuất hiện cảnh báo lỗi và không được tính toán điểm trong quá trình xử lý.
3. Chạy chương trình
3.1 Đọc file
  >>>run = the_class()
  >>>run.read_class()
Sau đó hãy nhập tên file dữ liệu của bạn, nếu bạn nhập đúng tên file, công cụ sẽ hiển thị thông báo đã đọc thành công
Nếu bạn nhập sai tên file, cảnh báo lỗi sẽ hiện ra và hỏi bạn có muốn thử nhập lại tên file không, nhập "y" để tiếp tục nếu có và "n" để thoát khỏi trương trình.
3.2 Phân tích file
  >>>run.ANALYZING()
  >>>run.Dap_An()
  >>>run.Check_dap_an()
- Khi hàm được thực thi, công cụ yêu cầu bạn nhập vào đáp án của bài kiểm tra (gồm 25 ký tự được phân tách bởi dấu ","), hãy nhập chuỗi đáp án của bạn và công cụ sẽ phân tích và đưa ra các báo cáo phân tích của tập dữ liệu:
3.4 Xuất file dữ liệu đã được phân tích.
  >>>run.export_file()
 - Để xuất dữ liệu gồm các dòng chứa mã ID và số điểm tương ứng dược chấm
