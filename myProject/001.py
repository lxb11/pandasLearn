#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd


def test01():
    people = pd.read_excel('D:/temp/people.xlsx', header=None)
    people.columns = ['Seq', 'ID', 'Name', 'Grade']
    print(people.shape)
    print(people.columns)
    print(people.head(4))
    print("-------------------------------------------------")
    print(people.tail(3))


def test02():
    people = pd.read_excel('D:/temp/people.xlsx', header=None)
    people.columns = ['Seq', 'ID', 'Name', 'Grade']
    # people = people.index('Seq')
    people.set_index('Seq', inplace=True)
    print(people.columns)
    people.to_excel('D:/temp/output.xlsx')
    print('Done!')


def test03():
    df = pd.read_excel('D:/temp/output.xlsx', index_col='Seq')
    df.to_excel('D:/temp/output2.xlsx')
    print("Done!")


def main():
    print("---main---")
    test03()


if __name__ == '__main__':
    main()
