import logging
import os
print(os.getcwd())


dir_path = r'E:\python\ineuron'
log_file = 'system.txt'

full_path = os.path.join(dir_path, log_file)

os.makedirs(dir_path, exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

#File handler
handler = logging.FileHandler(full_path)
handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s'))


logger.addHandler(handler)

def letUsCheckSystem(sys):
    if sys!= 'ok':
        logging.critical("system failure: %s ", sys)
letUsCheckSystem("no power suplly")
handler.close()



