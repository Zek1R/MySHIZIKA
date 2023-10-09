#include <iostream>
#include <windows.h>
#include <stdio.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251); // Ввод с консоли в кодировке 1251
    SetConsoleOutputCP(1251);
    cout << "Русский язык выводится корректно\n";

    int wigth = 80;
    string surName1 = "Иванов";
    string surName2 = "Ландау";
    string surName3 = "Дойль";
    string bName1 = "Потоп";
    string bName2 = "Механика";
    string bName3 = "Сумчатые";
    int bYear1 = 1978;
    int bYear2 = 1989;
    int bYear3 = 1990;
    string bGroup1 = "Х";
    string bGroup2 = "У";
    string bGroup3 = "С";
    string descr = "Х - художественная литература; У - учебная литература; С - справочная литература";

    char tmpC1[32];
    char tmpC2[32];
    char tmpC3[2];

    //Сенкевич Потоп 1978 Х
    printf("Введите: фамилию(1)    название(1)       год(1)      группу(1)\n");
    scanf_s("%s %s %d %s", tmpC1, sizeof(tmpC1), tmpC2, sizeof(tmpC2), &bYear1, tmpC3, sizeof(tmpC3));
    surName1 = tmpC1;
    bName1 = tmpC2;
    bGroup1 = tmpC3;


    //Ландау Механика 1989 У
    printf("Введите фамилию(2)    название(2)       год(2)      группу(2)\n");
    scanf_s("%s %s %d %s", tmpC1, sizeof(tmpC1), tmpC2, sizeof(tmpC2), &bYear2, tmpC3, sizeof(tmpC3));
    surName2 = tmpC1;
    bName2 = tmpC2;
    bGroup2 = tmpC3;

    //Дойль Сумчатые 1990 С
    printf("Введите фамилию(3)    название(3)       год(3)      группу(3)\n");
    scanf_s("%s %s %d %s", tmpC1, sizeof(tmpC1), tmpC2, sizeof(tmpC2), &bYear3, tmpC3, sizeof(tmpC3));
    surName3 = tmpC1;
    bName3 = tmpC2;
    bGroup3 = tmpC3;

    //Вывод
    printf("\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");
    printf("|Каталог библиотеки                                                            |\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");
    //                   28                     19              16                16
    printf("|Автор книги                |Название          |Год выпуска        |Группа     |");
    printf("\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");

    //Строка 1
    printf("|%s", surName1.c_str());
    for (int i = 0; i < 27 - surName1.size(); i++)
        printf(" ");
    printf("|%s", bName1.c_str());
    for (int i = 0; i < 18 - bName1.size(); i++)
        printf(" ");
    printf("|%d", bYear1);
    for (int i = 0; i < 15; i++)
        printf(" ");
    printf("|%s", bGroup1.c_str());
    for (int i = 0; i < 10; i++)
        printf(" ");
    printf("|\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");

    //Строка 2
    printf("|%s", surName2.c_str());
    for (int i = 0; i < 27 - surName2.size(); i++)
        printf(" ");
    printf("|%s", bName2.c_str());
    for (int i = 0; i < 18 - bName2.size(); i++)
        printf(" ");
    printf("|%d", bYear2);
    for (int i = 0; i < 15; i++)
        printf(" ");
    printf("|%s", bGroup2.c_str());
    for (int i = 0; i < 10; i++)
        printf(" ");
    printf("|\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");

    //Строка 3
    printf("|%s", surName3.c_str());
    for (int i = 0; i < 27 - surName3.size(); i++)
        printf(" ");
    printf("|%s", bName3.c_str());
    for (int i = 0; i < 18 - bName3.size(); i++)
        printf(" ");
    printf("|%d", bYear3);
    for (int i = 0; i < 15; i++)
        printf(" ");
    printf("|%s", bGroup3.c_str());
    for (int i = 0; i < 10; i++)
        printf(" ");
    printf("|\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");

    printf("Х - художественная литература; У - учебная литература; С - справочная литература");
    //for (int i = 0; i < wigth; i++)
        //printf(" ");
    printf("\n");
    for (int i = 0; i < wigth; i++)
        printf("-");
    printf("\n");

    return 0;
}