# python-mysqlconnector-class

Veritabanı işlemlerinizi Python üzerinde kolayca yapabilmeniz için bir sınıf geliştirildi. Bu sınıfı kullanarak bu işlemleri kolay ve rahat bir şekilde yapabilirsiniz. Bu sınıfın kurulumu ve kullanım şekilleri aşağıda yer almaktadır.

## Kurulum

Sınıfı kullanabilmeniz için aşağıdaki paketlerin kurulumunu yapmanız gerekmektedir. Paket kurulumları için [pip](https://pip.pypa.io/en/stable/) paketini öncelikle kurunuz

#### "pip" kullanımı -windows için

```bash
pip install "paket ismi"       -YA DA-      python -m pip install "paket ismi"
```

#### "pip" kurulumu -linux için

```bash
yum install epel-release 
yum install python-pip
```

#### "mysql-connector" kurulumu

```bash
pip install mysql-connector-python
```


## Kullanım

##### Kullanım sağlayacağınız sayfaya aşağıdaki şekilde dahil ediniz

```python
from coldrimpSql import coldrimpSql

connect = coldrimpSql()
print (connect)
```

# Örnek Kullanımlar

Aşağıda sınıf method'larını nasıl kullanabileceğiniz yer almaktadır.

## Örnek Veritabanı

```sql
CREATE TABLE `tabloadi` (
  `Id` bigint(22) NOT NULL,        #kolon
  `names` varchar(255) NOT NULL,   #kolon
  `fak` text NOT NULL              #kolon
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```


## SELECT 

```python
from coldrimpSql import coldrimpSql

connect = coldrimpSql()

## WHERE tanımında parametrelerin "AND" kullanımı için aşağıdaki şekilde uygulanmalı
testWhereAND = {
    'Id': '1',
    'names': 'Ahmet'
}

## WHERE tanımında parametrelerin "OR" kullanımı için aşağıdaki şekilde uygulanmalı
testWhereOR = [
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


testConnection = connect.Select('tabloadi', 'where');

print(testConnection)
```

##### -WHERE- OR kullanımı
```python

testConnection = connect.Select( 'tabloadi', testWhereOR );

```

##### -WHERE- AND kullanımı
```python

testConnection = connect.Select( 'tabloadi', testWhereAND );

```
##### -WHERE- TEK kullanımı
```python

testConnection = connect.Select( 'tabloadi', 'ID=1');

```


## INSERT


```python


testInsertData = {
    'Id': '1', #veritabanı kolon
    'names': 'Ahmet' #veritabanı kolon
}

testConnection = connect.Insert('tabloadi', testInsertData )


```



## UPDATE 

```python
from coldrimpSql import coldrimpSql

connect = coldrimpSql()

## Değişim sağlanacak kolonların adi ve değerleri aşağıdaki şekilde tanımlanmalıdır.

testUpdate = {
    'names': 'Ahmet',
    'fak': 'test-fak'
}


testConnection = connect.Update('tabloadi', testUpdate, 'Id=1')
print(testConnection)

```

## DELETE 

```python
from coldrimpSql import coldrimpSql

connect = coldrimpSql()


testDeleteParams = {
    'Id' : [  # Id hangi kolon üzerinde silim işlemi uygulanacaksa o kolonun ismi
        '94', '113', '114' # silim işlemi yapılacak hedef veri bilgileri "çoklu ya da tek değer girilebilir"
    ]
}

testDelete = connect.Delete('tabloadi', testDeleteParams)
testDelete2 = connect.Delete('tabloadi', 'Id=1') # tek 1 veri silineceğinde kullanılabilir

print(testDelete)

print(testDelete2)

```



## License
[MIT](https://choosealicense.com/licenses/mit/)