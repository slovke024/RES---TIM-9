import unittest
import klase
from unittest.mock import patch
from ReplicatorReciver import pakovanje
from client import vremenski_interval,poslednja_vrednost


class TestReader(unittest.TestCase):

    #@patch('klase.RecieverProperty.__init__')
    def test_recieverProperty(self):
        with patch('klase.RecieverProperty.__init__') as mock_init:
            #rc = klase.RecieverProperty.__init__(self,'CODE_ANALOG', 13)
            rc = mock_init(self,'CODE_ANALOG',13)
            self.assertEqual(mock_init.call_args[0][1], 'CODE_ANALOG')
            self.assertEqual(mock_init.call_args[0][2], 13)


            rc1 = mock_init(self,'CODE_SINGLENOE',46)
            self.assertEqual(mock_init.call_args[0][1], 'CODE_SINGLENOE')
            self.assertEqual(mock_init.call_args[0][2], 46)

    
    def test_collectionDescription(self):
        with patch('klase.CollectionDescription.__init__') as mock_init2:
            rc1 = klase.RecieverProperty("CODE_ANALOG", 10)
            rc2 = klase.RecieverProperty("CODE_CUSTOM", 29)
            rc3 = klase.RecieverProperty("CODE_CONSUMER", 40)
            historical = list()
            historical.append(rc1)
            historical.append(rc2)
            historical.append(rc3)

            cd = mock_init2(self, 1, 2, historical)

            self.assertEqual(mock_init2.call_args[0][1],1)
            self.assertEqual(mock_init2.call_args[0][2],2)
            self.assertEqual(mock_init2.call_args[0][3],historical)
            

    def test_reader_init(self):
         with patch('klase.Reader.__init__') as mock_init:
        
            read_init = mock_init(self, 'Dataset1')

            self.assertEqual(mock_init.call_args[0][1],'Dataset1')

    def test_reader_upisUBazu(self):
        with patch('klase.Reader.upisiUBazu') as mock_upis:

            mock_upis(self, 'CODE_SOURCE', 45)
            mock_upis.return_value=True
            assert mock_upis(self,'CODE_SOURCE', 45)
            self.assertEqual(mock_upis.call_args[0][1],'CODE_SOURCE')
            self.assertEqual(mock_upis.call_args[0][2],45)

    def test_reader_poslednjaVrednost(self):
        with patch('klase.Reader.poslednjaVrednost') as mock_poslednja:
            
            mock_poslednja(self, 'CODE_DIGITAL')
            mock_poslednja.return_value=True
            assert mock_poslednja(self, 'CODE_DIGITAL')
            self.assertEqual(mock_poslednja.call_args[0][1],'CODE_DIGITAL')

    def test_reader_vremenskiInterval(self):
        with patch('klase.Reader.vremenskiInterval') as mock_interval:

            mock_interval(self,'CODE_SOURCE','2022/6/19','2022/6/21')
            mock_interval.return_value=True
            assert mock_interval(self,'CODE_SOURCE','2022/6/19','2022/6/21')
            self.assertEqual(mock_interval.call_args[0][1],'CODE_SOURCE')
            self.assertEqual(mock_interval.call_args[0][2],'2022/6/19')
            self.assertEqual(mock_interval.call_args[0][3],'2022/6/21')


    def test_logger_msg(self):
        with patch('klase.Logger.upisiLog') as mock_logger:
            mock_logger(self, 'poruka')
            mock_logger.return_value=True
            assert mock_logger(self, 'poruka')
            self.assertEqual(mock_logger.call_args[0][1],'poruka')

    def test_codeValue(self):
        with patch('klase.CodeValue.__init__') as mock_init:
            #rc = klase.RecieverProperty.__init__(self,'CODE_ANALOG', 13)
            cv = mock_init(self,'CODE_LIMITSET',99)
            self.assertEqual(mock_init.call_args[0][1], 'CODE_LIMITSET')
            self.assertEqual(mock_init.call_args[0][2], 99)


            cv1 = mock_init(self,'CODE_DIGITAL',6)
            self.assertEqual(mock_init.call_args[0][1], 'CODE_DIGITAL')
            self.assertEqual(mock_init.call_args[0][2], 6)

    def test_replicatorReciver_pakovanje(self):
        with patch('ReplicatorReciver.pakovanje') as mock_pakovanje:
            mock_pakovanje(('CODE_ANALOG',15))
            mock_pakovanje.return_value=True
            p=('CODE_ANALOG',15)
            assert mock_pakovanje(('CODE_ANALOG',15))
            self.assertEqual(mock_pakovanje.call_args[0][0][0],p[0])
            self.assertEqual(mock_pakovanje.call_args[0][0][1],p[1])

    def test_Reader_deadband(self):
        with patch('reader.deadband') as mock_deadband:
            mock_deadband('CODE_ANALOG',15)
            mock_deadband.return_value=True
            self.assertEqual(mock_deadband.call_args[0][0],'CODE_ANALOG')
            self.assertEqual(mock_deadband.call_args[0][1],15)
            assert mock_deadband('CODE_ANALOG',15)

    def test_client_vremenskiInterval(self):
        with patch('client.vremenski_interval') as mock_vremenskiInterval:
            mock_vremenskiInterval()
            mock_vremenskiInterval.return_value=True
            assert mock_vremenskiInterval()

    def test_client_poslednjaVrednost(self):
        with patch('client.poslednja_vrednost') as mock_poslednjaVrednost:
            mock_poslednjaVrednost()
            mock_poslednjaVrednost.return_value=True
            assert mock_poslednjaVrednost()


if __name__ == '__main__':
    unittest.main()