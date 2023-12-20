# Mphasis-optimization - Inter IIT Midprep (Team 41)

## Abstract

Airlines routinely change their flight schedules for various reasons like seasonal demands,
picking new routes, time changes needed based on daylight savings, changes to flight numbers,
operating frequency, timings, etc. Many passengers will be impacted due to these schedule
changes and they need to re-accommodate to the alternate flights. Airlines need a solution to
analyze the impact on the passengers with their planned schedule changes and automatically
identify suitable alternate flights for the impacted passengers

## Objective

Identify optimal/best alternate flight solutions for all the impacted passengers (impacted
due to planned schedule change) based on the provided rule sets. Also, ensuring the validity
of the solution with all the rule sets enforced. Rank the solutions based on various factors
like time to reach the destination, impact on the purchased ancillary services, etc. as well as
include Ranking of passengers on the solution based on re-accommodation priority based on
factors like passenger type (unaccompanied minor, on duty employee, loyalty customer levels,
paid class of service, etc). You can enforce the rule sets as part of optimization constraints or
as pre or post-process calculation

## Remarks

- ~ 30 Affected flight solutions found / second (4 core CPU)
- One time pre-processing, Faster searching
- Assumption - # of connecting flights have a low maximum 
limit: Constant order depth first search
- Flexibility in PNR & Flight scoring
- Continuous scoring functions - Accurate score for filtering 
the top paths

## Flowchart of the application

### Input

![Input flowchart](images/input.png?raw=true "Title")

### Initialize Depth First Search

![DFS flowchart](images/dfs.png?raw=true "Title")

### Flight Scoring

![Flight scoring flowchart](images/flight_scoring.png?raw=true "Title")

### Passenger scoring

![Passenger scoring flowchart](images/passenger_scoring.png?raw=true "Title")

### Passenger accomodation

![Passenger accommodation flowchart](images/accommodation.png?raw=true "Title")

### Storing the output and bulk mailing

![Output flowchart](images/output_mailing.png?raw=true "Title")

## Setup

### Install virtual environment package
```bash

pip install virtualenv

```

### Change the directory to project directory

```bash

cd $PROJECT_DIR

```

### Create a virtual environment

#### For UNIX systems
```bash

virtualenv env

```

#### For Windows
```bash

python -m virtualenv env

```

### Start the virtual environment

#### For UNIX systems
```bash

source env/bin/activate

```

#### For Windows
```bash

.\env\Scripts\activate

```

### Install the requirements

```bash

pip install -r requirements.txt

```

### Run the application

```bash

python main.py

```
