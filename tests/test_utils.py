import unittest
import os
from app.utils import load_yaml_config, generate_logs_from_config

class TestUtils(unittest.TestCase):

    def test_load_yaml_config(self):
        config = load_yaml_config('config/logs_config.yml')
        self.assertIn('logs', config)

    def test_generate_logs_from_config(self):
        config = {
            'logs': [
                {'type': 'auth', 'output_file': '../generated_logs/test_auth.log', 'log_count': 10},
                {'type': 'failed_auth', 'output_file': '../generated_logs/test_failed_auth.log', 'log_count': 5}
            ]
        }
        generate_logs_from_config(config)

        # Vérifiez si les fichiers de sortie existent
        self.assertTrue(os.path.exists('../generated_logs/test_auth.log'))
        self.assertTrue(os.path.exists('../generated_logs/test_failed_auth.log'))

        # Nettoyez les fichiers générés après le test
        os.remove('../generated_logs/test_auth.log')
        os.remove('../generated_logs/test_failed_auth.log')

if __name__ == '__main__':
    unittest.main()
