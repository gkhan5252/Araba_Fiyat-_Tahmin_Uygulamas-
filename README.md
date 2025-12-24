# 🚗 Car Price Prediction with Multiple Linear Regression & Flask

Bu proje, bir araç satış veri seti üzerinde **Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli kurmayı ve
eğitilen modeli **Flask tabanlı bir web arayüzü** üzerinden kullanıcıya sunmayı amaçlamaktadır.

Proje, makine öğrenmesi modelleme sürecinin **veri ön işleme → modelleme → değerlendirme → dağıtım (deployment)** adımlarını
uçtan uca kapsamaktadır.

---

## 📌 Kullanılan Teknolojiler

- Python 3.x  
- Pandas, NumPy  
- Scikit-learn  
- Statsmodels  
- Flask  
- Joblib  
- Jupyter Notebook  

---

## 📂 Proje Dosya Yapısı

# 🚗 Car Price Prediction with Multiple Linear Regression & Flask

Bu proje, bir araç satış veri seti üzerinde **Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli kurmayı ve
eğitilen modeli **Flask tabanlı bir web arayüzü** üzerinden kullanıcıya sunmayı amaçlamaktadır.

Proje, makine öğrenmesi modelleme sürecinin **veri ön işleme → modelleme → değerlendirme → dağıtım (deployment)** adımlarını
uçtan uca kapsamaktadır.

---

## 📌 Kullanılan Teknolojiler

- Python 3.12.6  
- Pandas, NumPy  
- Scikit-learn  
- Statsmodels  
- Flask  
- Joblib  
- Jupyter Notebook  

3️⃣ Backward Elimination (Geriye Doğru Eleme)

Modelde istatistiksel olarak anlamsız öznitelikleri elemek için
Backward Elimination yöntemi uygulanmıştır.

Adımlar:

Tüm özelliklerle OLS modeli kuruldu

p-value değerleri incelendi

p > 0.05 olan değişkenler modelden çıkarıldı

📌 Bu işlem statsmodels kütüphanesi ile yapılmıştır.

4️⃣ Model Kurulumu

Model: Multiple Linear Regression

Kütüphane: sklearn.linear_model.LinearRegression

Eğitim/Test oranı: %80 / %20

5️⃣ Model Değerlendirme

Model aşağıdaki metriklerle değerlendirilmiştir:

R² (R-Kare)

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

Örnek çıktı:

R² Score : 0.38
MAE      : 221927
MSE      : 187062423101


📌 R² değerinin sınırlı olmasının nedeni:

Veri setindeki fiyatların geniş aralıkta olması

Lineer modelin karmaşık fiyat ilişkilerini tam yakalayamaması

6️⃣ Modelin Kaydedilmesi

Eğitilen model ve scaler aşağıdaki formatta kaydedilmiştir:

joblib.dump(model, "car_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")


Bu dosyalar Flask uygulamasında doğrudan kullanılmaktadır.

7️⃣ Flask Web Arayüzü

Flask ile basit ve işlevsel bir web arayüzü geliştirilmiştir.

Özellikler:

Kullanıcıdan araç bilgilerini alır

Eğitilmiş modeli kullanarak fiyat tahmini yapar

Sonucu web sayfasında gösterir

Uygulamayı çalıştırmak için:

python app.py


Tarayıcıdan erişim:

http://127.0.0.1:5000

8️⃣ Sonuç ve Değerlendirme

Bu projede:

Çoklu doğrusal regresyon başarıyla uygulanmıştır

Veri ön işleme adımları detaylı şekilde gerçekleştirilmiştir

Backward Elimination ile model sadeleştirilmiştir

Model bir Flask arayüzü ile son kullanıcıya sunulmuştur

---

## 📂 Proje Dosya Yapısı

