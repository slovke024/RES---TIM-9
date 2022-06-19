import unittest
import klase
from unittest.mock import patch

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
        with patch('klase.CollectionDescription.__init__') as mock_init:

            rc1 = klase.RecieverProperty("CODE_ANALOG", 10)
            rc2 = klase.RecieverProperty("CODE_CUSTOM", 29)
            rc3 = klase.RecieverProperty("CODE_CONSUMER", 40)
            historical = list()
            historical.append(rc1)
            historical.append(rc2)
            historical.append(rc3)

            cd = mock_init(self, 1, 2, historical)

            self.assertEqual(mock_init.call_args[0][1],1)
            self.assertEqual(mock_init.call_args[0][2],2)
            self.assertEqual(mock_init.call_args[0][3],historical)

    def test_reader_init(self):
         with patch('klase.Reader.__init__') as mock_init:
        
            read_init = mock_init(self, 'Dataset1')

            self.assertEqual(mock_init.call_args[0][1],'Dataset1')

    def test_reader_upisUBazu(self):
        with patch('klase.Reader.upisiUBazu') as mock_upis:

            inputDB = mock_upis(self, 'CODE_SOURCE', 45)

            self.assertEqual(mock_upis.call_args[0][1],'CODE_SOURCE')
            self.assertEqual(mock_upis.call_args[0][2],45)

    def test_reader_poslednjaVrednost(self):
        with patch('klase.Reader.poslednjaVrednost') as mock_poslednja:
            
            poslednja = mock_poslednja(self, 'CODE_DIGITAL')
            self.assertEqual(mock_poslednja.call_args[0][1],'CODE_DIGITAL')

    def test_reader_vremenskiInterval(self):
        with patch('klase.Reader.vremenskiInterval') as mock_interval:

            interval = mock_interval(self,'CODE_SOURCE','2022/6/19','2022/6/21')
            self.assertEqual(mock_interval.call_args[0][1],'CODE_SOURCE')
            self.assertEqual(mock_interval.call_args[0][2],'2022/6/19')
            self.assertEqual(mock_interval.call_args[0][3],'2022/6/21')


    def test_logger_msg(self):
        with patch('klase.Logger.upisiLog') as mock_logger:
            logger = mock_logger(self, 'poruka')

            self.assertEqual(mock_poslednja.call_args[0][1],'poruka')


            


if __name__ == '__main__':
    unittest.main()