from coldrimpSql import coldrimpSql

connect = coldrimpSql()


testInsertParams = {
    'names': 'ahmet',
    'fak' : 'testFak'
}

testUpdateParams = {
    'names': 'ahmet',
    'fak' : 'testFak'
}

testSelectParams = [
    {
        'Id': '94'
    },
    {
        'Id': '100'

    },
    {
        'Id': '101'
    }
]

testDeleteParams = {
    'Id' : [
        '94', '113', '114'
        ]
}

testSelect = connect.Select('tabloadi', testSelectParams)
testInsert = connect.Insert('tabloadi', testInsertParams)
testUpdate = connect.Update('tabloadi', testUpdateParams, 'Id=94')
testDelete = connect.Delete('tabloadi', testDeleteParams)
testDelete2 = connect.Delete('tabloadi', 'Id=115')


print(testDelete2)
