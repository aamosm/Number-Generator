# Custom Number Generator

A Python utility designed to generate large, customizable datasets of random numbers.

### Context
I built this tool to assist with mathematical testing, specifically for analyzing convergence patterns related to **Kaprekar's constant (6174)**. The standard libraries didn't offer the specific formatting or volume control I needed for rapid iteration, so I wrote this script to handle the data generation.

### Usage

#### 1. Automated Generation (GitHub Actions)
This repository utilizes a **GitHub Actions workflow** to generate datasets in the cloud.
* **Trigger:** The workflow runs automatically on push [or specify: on a schedule/manually via the Actions tab].
* **Output:** The script generates a new dataset and automatically **commits the results directly to this repository**.
* **Location:** Check the latest commit history or the root directory for the updated output file.

#### 2. Local Execution
To generate numbers on your local machine:

```bash
python main.py
