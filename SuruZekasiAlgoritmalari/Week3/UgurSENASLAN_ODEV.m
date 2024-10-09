% 1) A matrisini giriniz
A = [1 3 5; 7 8 11; 100 1 4] 

% 2) A matrisinin determinantı
A_det = det(A)

% 3) A matrisinin tersini bulunuz. Çıkan sonucu bir B matrisine atayınız
B = inv(A)

% 4) A*B işlemini yapınız. Elde dilen sonucu irdeleyiniz.

disp(A * B) 
    % Bir matrisin kendisini ve tersi çarpıldığında birim matris elde edilir

% 5) A Matrisinin 1. sütununu a1, 3. sütununu a3 verktörüne atayınız

a1 = A(:,1)
a3 = A(:,3)

% 6) Köşegenleri A matrisinin köşegenlerinden oluşan bir C köşegen matrisi
% oluşturunuz

C = diag(A)


% 7) a1'in devriği ile a3 vektörünü çarpınız

a1_devr = a1'
disp(a1_devr * a3)

% 8) a1 ile a3 vektör elemanlarını karşılıklı çarpınız

disp(a1.*a3)

% 9) A'nın 3.satırını, diğer elemanlarını girmeden [5 6 7] olarak
% değiştiriniz

A(3,:) = [5 6 7]

% 10) A'nın 1 ve 2. satırlarını siliniz

A(1,:) = []
A(2,:) = []