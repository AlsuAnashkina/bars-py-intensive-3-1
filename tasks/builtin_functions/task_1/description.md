Реализовать класс *Value*, которое принимает числовое значение. Класс *Value* должен
уметь быть частью простейших арифметических действий (сложение/вычитание, умножение/деление).
В случае невозможности выполнения действий - выбрасывать исключение *MyException*(tasks/common).
Пример:
> ten = Value(10) 
>
> ten + 2  # -> 12 
> 
> ten / 2  # -> 5 
 