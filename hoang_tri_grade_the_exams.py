
import numpy as np
import pandas as pd
import re
class the_class:
    def __init__(self):
        pass

    def nhaclai_user(self): 
        while True:
            nhaclai = input("Bạn có muốn tiếp tục không (1=yes/0=no)\n")
            if nhaclai == "1" :
                return True
            else:
                return False

    def read_class(self): # đọc file
        while True:
            file_name = input("\n"+"Enter a file name :")
            try:
                data_input = pd.read_csv(file_name, on_bad_lines="skip",sep=",",header=None) # bỏ qua những dòng null
                data_input = data_input[0].str.split(',',expand=True) # lấy các mã sinh viên
                print("Successfully opened" + file_name +"\n")
                self.data_input = data_input
                self.file_name = file_name
                break
            except Exception as e:# in ra ngoại lệ nếu có
                print(e)
                print("Sorry, I can't find this filename")
                xac_nhan = self.nhaclai_user()
                if xac_nhan == False:
                    print("Kết thúc chương trình")
                    break
                    
                    
    def ANALYZING(self): # Phân tích các dòng hợp lệ
      print("\n**** ANALYZING ****\n")
      df = pd.read_csv(self.file_name, sep=' ' ,header=None) # đưa hết về 1 cột để phân tích
      self.df=df
      error_vaild_26 = [] # list lỗi không đủ 26 cột
      error_vald_N = [] # list lỗi ký tự N# mã sinh viên
      for i in range(len(df)):
        c = (df[0][i]).split(sep=",") # tra từng hàng 
        if len(c) != 26:
          print("Invalid line of data: does not contain exactly 26 values: \n",df[0][i])
          error_vaild_26.append(c)
          df.drop(index=[i], inplace=True) # xóa index[i] trong df
        if len(c[0]) !=9:
          print("Invalid line of data: N# is invalid: \n", df[0][i])
          error_vald_N.append(c)
          df.drop(index=[i], inplace=True) 
        elif len(c[0]) == 9:
          regex = re.compile(r'^N(\d{8})$') # ký tự ^ là bắt đầu một string, sau đó phải đến ký tự "N". \d{8}: định nghĩa nó = 8 ký tự số sau đó.$: kết thúc 1 str 
          if bool(regex.match(c[0])) == False:
            print("Invalid line of data: N# is invalid: \n", df[0][i])
            error_vald_N.append(c)
            df.drop(index=[i], inplace=True) 
      if len(error_vaild_26) + len(error_vald_N) ==0: 
        print("No errors found!") 
      print("\n**** REPORT ****\n")
        # df.values
      print("Total valid lines of data: {}".format(len(df))) # các dòng hợp lệ
      print("Total invalid lines of data: {}".format(len(error_vaild_26) + len(error_vald_N))) # các dòng không hợp lệ
    
    
    def Dap_An(self): # nhập đán án mẫu
        while True:
            try:
                answer_key = input("Nhap answer_key, nhap du 25 dap an: ").split(",")
                self.answer_key = answer_key
               
                if len(self.answer_key)==25:
                    break
                else:
                    print("Nhap dap an khong hop le") 
                    if self.nhaclai_user == False:
                        print(" Ket thuc chuong trinh")
                        break
            except:
                if self.nhaclai_user == False:
                    print("Ket thuc chuong trinh")
                    break
            print(answer_key)
            
            
    def Check_dap_an(self): # chấm điểm
        diem_tong = []
        for i in self.df.index.values:
            dapan_sinhvien = self.df[0][i].split(sep=",") # lấy từng dòng của df
            score = 0
            for j in range(1,26):
                    if self.answer_key[j-1] == dapan_sinhvien[j]: # len của đáp án sinh viên = 26, len của đáp án = 25
                      score = score + 4
                    elif dapan_sinhvien[j] == "":
                      None
                    else:
                      score = score - 1
            diem_tong.append(score)
        # print(self.df)
        self.df["score"] = diem_tong # tạo 1 cột bằng điểm đã tính của từng dòng
        print("Mean (average) score: ", self.df["score"].mean())
        print("Highest score: ", self.df["score"].max())
        print("Lowest score: ", self.df["score"].min())
        print("Range of scores: ", self.df["score"].max()-self.df["score"].min())
        print("Median score: ", int(self.df["score"].median()))
        
        
    def export_file(self):
      self.df['ma_sv'] = self.df.iloc[:,0].apply (lambda x: x.split (',')[0]) # tạo cột mã sinh viên 
      file_name2 = self.file_name[:len(self.file_name)-4] + "_grades.txt" # tạo tên ghi file
      self.df[["ma_sv","score"]].to_csv(file_name2, header=None, index=None, sep=',', mode='a') # tạo file mới từ 2 cột mã sv và điểm 

# run = the_class()
# run.read_class()
# run.ANALYZING()
# run.Dap_An()
# run.Check_dap_an()
# run.export_file()
