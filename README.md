# Container Environment for Selenium Python Tests development

The setup includes a host which has selenium and chrome installed.

The tests will reside in another container and will run remotely on the selenium host

## Services:

### Selenium
From official selenium image.

### Tests Integration
Where the tests reside

## Start the setup
`docker-compose up --build`

## Start the Selenium Host
Using VNC on `localhost:5901` and password `secret`

## Run the tests after changes
    docker-compose exec test-integration bash
    root@8954656e2a32:/selenium-python_wks# pytest -s -v
