#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd


def test01():
    products = pd.read_excel('D:/temp/List.xlsx', index_col='ID')
    products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[True, False])
    print(products)


def test02():
    students = pd.read_excel('D:/temp/Students.xlsx', index_col='ID')
    # students = students.loc[students['Age'].apply(ID_18_to_30)].loc[students['Score'].apply(level_a)]
    # students = students.loc[students.Age.apply(ID_18_to_30)].loc[students.Score.apply(level_a)]
    students = students.loc[students.Age.apply(lambda a:100071000014924 <= a < 104911120312178)]. \
        loc[students.Score.apply(lambda s: 345 <= s <= 400)]

    print(students)


def main():
    print("---main---")
    test02()


if __name__ == '__main__':
    main()
