#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


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


def test03():
    students = pd.read_excel('D:/temp/StudentsMajor.xlsx')
    students.sort_values(by='Number', inplace=True, ascending=False)
    print(students)
    # students.plot.bar(x='Field', y='Number', color='orange')
    plt.bar(students.Field, students.Number, color='orange')
    plt.xticks(students.Field, rotation='90')
    plt.xlabel('Filed')
    plt.ylabel('Number')
    plt.title('International Students by Field', fontsize=16)
    plt.tight_layout()
    plt.show()


def test04():
    students = pd.read_excel('D:/temp/Student10.xlsx')
    students.sort_values(by='str2017', inplace=True, ascending=False)
    print(students)
    students.plot.bar(x='Field', y=['str2016', 'str2017'], color=['orange', 'red'])
    plt.title('International Students by Field', fontsize=16, fontweight='bold')
    plt.xlabel('Field', fontweight='bold')
    plt.ylabel('Number', fontweight='bold')
    ax = plt.gca()
    ax.set_xticklabels(students['Field'], rotation=45, ha='right')
    f = plt.gcf()
    f.subplots_adjust(left=0.2, bottom=0.42)
    plt.tight_layout()
    plt.show()


def main():
    print("---main---")
    test04()


if __name__ == '__main__':
    main()
