﻿Program meridian;
var l, R, z: real;
x:longint;
begin
l:=111321.37; //  расстояние между соседними меридианами на экваторе в метрах
R:=0; //расстояние между соседними меридианами с произвольными координатами в метрах (пока неизвестно)
z:=0; // расстояние, в 60 раз меньшее расстояния между соседними меридианами с произвольными координатами в метрах (пока неизвестно)
writeln('Введите x - градус широты');
readln(x);
if abs(x)>90 then begin
            writeln('Неверное число, попробуйте сначала');
            end;
if (x>0) and (x<90) then begin
            R:=l*cos(x*pi/180);
            z:=R/60;
            writeln('Длина 1 минуты дуги меридиана северной широты равна ');
            end;
if (x<0) and (x>(-90)) then begin
            R:=l*abs(cos(x*pi/180));
            z:=R/60;
            writeln('Длина 1 минуты дуги меридиана южной широты равна ');
            end;
if (x=0) then begin
            z:=l/60;
            writeln('Длина 1 минуты дуги меридиана экватора равна ');
            end;
if (abs(x)=90) then begin
            writeln('Вы находитесь на одном из полюсов Земли, можете этим гордиться');
            end;
write(z:0:2);
end.