## Set Up

### For Ubuntu
`sudo apt install python3.10-venv`

### Create Virual Environment
- windows - `py -m venv venv`
- ubuntu - `python3 -m venv venv`

### Activate Vritual Environment
- windows - `.\venv\Scripts\activate`
- ubuntu - `source venv/bin/activate`

### Install Flask
- windows - `pip install Flask`
- ubuntu - `pip install Flask`
- If you get error: Command 'pip' not found
run `sudo apt install python3-pip`

### Run App
- `flask --app app run --debug`