from csv import reader
from http import client
import unittest
from klase import *
from unittest.mock import patch
from ReplicatorReciver import pakovanje
from reader import deadband



class TestReader(unittest.TestCase):

    #@patch('klase.RecieverProperty.__init__')
    def test_recieverProperty(self):
        with patch('klase.RecieverProperty') as mock_init:
            #rc = klase.RecieverProperty.__init__(self,'CODE_ANALOG', 13)
            mock_init(self,'CODE_ANALOG',13)
            rc=RecieverProperty('CODE_ANALOG',13)
            self.assertEqual(mock_init.call_args[0][1],rc.code)
            self.assertEqual(mock_init.call_args[0][2],rc.value)

    def test_collectionDescription(self):
        with patch('klase.CollectionDescription') as mock_cd:
            lista=list()
            lista.append(('CODE_DIGITAL',20))
            lista.append(('CODE_SINGLENOE',20))
            lista.append(('CODE_ANALOG',20))
            mock_cd(self,1,'DataSet1',lista)
            cd=CollectionDescription(1,'DataSet1',lista)
            self.assertEqual(mock_cd.call_args[0][1],cd.id)
            self.assertEqual(mock_cd.call_args[0][2],cd.data_set)
            self.assertEqual(mock_cd.call_args[0][3],cd.historical_collection)
            
       
    def test_reader_init(self):
         with patch('klase.Reader') as mock_init:
        
            mock_init(self, 'DataSet1')
            r=Reader('DataSet1')

            self.assertEqual(mock_init.call_args[0][1],r.dataSet)

    def test_reader_upisUBazu(self):
        with patch('klase.Reader') as mock_upis:

            r=Reader('DataSet4')
            mock_upis(self,'DataSet4')
            vrednost= r.upisiUBazu('CODE_SOURCE',45)
            self.assertEqual(mock_upis.call_args[0][1],r.dataSet)
            self.assertTrue(vrednost)

    def test_reader_poslednjaVrednost(self):
        with patch('klase.Reader') as mock_poslednja:
            
            mock_poslednja(self,'DataSet1')
            r=Reader('DataSet1')
            vrednost=r.poslednjaVrednost('CODE_ANALOG')
            self.assertEqual(mock_poslednja.call_args[0][1],r.dataSet)
            self.assertTrue(vrednost)

    def test_reader_vremenskiInterval(self):
        with patch('klase.Reader') as mock_interval:

            mock_interval(self,'DataSet1')
            r=Reader('DataSet1')
            
            vrednost=r.vremenskiInterval('CODE_ANALOG','2022-06-14 20:21:00','2022-06-14 21:21:00')
            self.assertEqual(mock_interval.call_args[0][1],r.dataSet)
            self.assertTrue(vrednost)

    def test_logger_msg(self):
        with patch('klase.Logger') as mock_logger:
            mock_logger(self)
            loger=Logger()
            vrednost = loger.upisiLog('poruka')
            self.assertTrue(vrednost)

    def test_codeValue(self):
        with patch('klase.CodeValue') as mock_init:
            #rc = klase.RecieverProperty.__init__(self,'CODE_ANALOG', 13)
            mock_init(self,'CODE_LIMITSET',99)
            cv=CodeValue('CODE_LIMITSET',99)
            self.assertEqual(mock_init.call_args[0][1], cv.code)
            self.assertEqual(mock_init.call_args[0][2], cv.value)


            mock_init(self,'CODE_DIGITAL',6)
            cv1 = CodeValue('CODE_DIGITAL',6)
            self.assertEqual(mock_init.call_args[0][1],cv1.code)
            self.assertEqual(mock_init.call_args[0][2], cv1.value)

    def test_replicatorReciver_pakovanje(self):
        with patch('ReplicatorReciver.pakovanje') as mock_pakovanje:
            mock_pakovanje(('CODE_ANALOG',15))
            p=('CODE_ANALOG',15)
            vrednost=pakovanje(p)
            self.assertEqual(mock_pakovanje.call_args[0][0][0],p[0])
            self.assertEqual(mock_pakovanje.call_args[0][0][1],p[1])
            self.assertTrue(vrednost)

            mock_pakovanje(('CODE_CUSTOM',15))
            p=('CODE_CUSTOM',15)
            vrednost=pakovanje(p)
            self.assertEqual(mock_pakovanje.call_args[0][0][0],p[0])
            self.assertEqual(mock_pakovanje.call_args[0][0][1],p[1])
            self.assertTrue(vrednost)

            mock_pakovanje(('CODE_SINGLENOE',15))
            p=('CODE_SINGLENOE',15)
            vrednost=pakovanje(p)
            self.assertEqual(mock_pakovanje.call_args[0][0][0],p[0])
            self.assertEqual(mock_pakovanje.call_args[0][0][1],p[1])
            self.assertTrue(vrednost)

            mock_pakovanje(('CODE_SOURCE',15))
            p=('CODE_SOURCE',15)
            vrednost=pakovanje(p)
            self.assertEqual(mock_pakovanje.call_args[0][0][0],p[0])
            self.assertEqual(mock_pakovanje.call_args[0][0][1],p[1])
            self.assertTrue(vrednost)

    def test_Reader_deadband(self):
        with patch('reader.deadband') as mock_deadband:
            mock_deadband('CODE_ANALOG',15)
            vrednost=deadband('CODE_ANALOG',15)
            self.assertEqual(mock_deadband.call_args[0][0],'CODE_ANALOG')
            self.assertEqual(mock_deadband.call_args[0][1],15)
            self.assertTrue(vrednost)
            vrednost=deadband('CODE_CUSTOM',15)
            self.assertTrue(vrednost)
            vrednost=deadband('CODE_SINGLENOE',15)
            self.assertTrue(vrednost)
            vrednost=deadband('CODE_SOURCE',15)
            self.assertTrue(vrednost)
           

if __name__ == '__main__':
    unittest.main()