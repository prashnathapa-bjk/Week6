
from tqdm import tqdm
import time

print("Starting your study tasks...")

for i in tqdm(range(20), desc="Study Progress"):
    time.sleep(0.05)

print("\nAll 20 study tasks completed successfully!")

