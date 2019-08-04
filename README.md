# python_ahrefs_api

Forked from [ahrefs-api-python]{https://github.com/spremotely/ahrefs-api-python}.

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

### Installing

```python
pip install python_ahrefs_api
```

### Usage
```python
import python_ahrefs_api

api = AhrefsApi('http://apiv2.ahrefs.com', 'b92188dg02d24dwc39ecdv0861fbb1eeac8c3g8c')
ahrefs_rank_result = api.ahrefs_rank('example.net').order_by('url:asc').where('url="http://example.net/"').get()
```

where b92188dg02d24dwc39ecdv0861fbb1eeac8c3g8c is your token

## Built With

* Love 

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Use [SemVer](http://semver.org/) for versioning. 

## Authors

* **John Petrilli** - *work* - [johnnyfireball](https://github.com/johnnyfireball)
* **spremotely** - *Original work* - [spremotely](https://github.com/spremotely)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Original Author: sp.remotely dev.sergey.popov@gmail.com
    url='https://github.com/spremotely/ahrefs-api-python',
* etc
