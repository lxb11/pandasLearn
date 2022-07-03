#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


def test01():
    users = pd.read_excel('D:/temp/Users.xlsx')
    users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
    users.sort_values(by='Total', inplace=True, ascending=True)
    print(users)
    users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
    plt.tight_layout()
    plt.show()


def test02():
    students = pd.read_excel('D:/temp/Student011.xlsx', index_col='From')
    print(students)
    students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
    plt.title('Source of International Students', fontsize=16, fontweight='bold')
    plt.ylabel('2017', fontsize=12, fontweight='bold')
    plt.show()


def test03():
    result = 0
    for i in range(0, 100):
        result += i
    print(result)


def main():
    print("---main---")
    test03()


if __name__ == '__main__':
    main()
