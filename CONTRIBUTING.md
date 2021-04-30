# Contributing to this repository

## Getting started

Before you begin:
-   Python 3.8 is used for this project.
-   For EPAM employees only: have you read the [Best Practices for Managing Secrets](https://elearn.epam.com/courses/course-v1:EPAM+5SCSS+0620/courseware/4b94c749c309409ea878fb7916be316b/ae4553f7cd524229b42f260b0ac692ed/1?activate_block_id=block-v1%3AEPAM%2B5SCSS%2B0620%2Btype%40vertical%2Bblock%40c04f1498c7d04ac4bf87b652741d90bb)?
-   Check out the [existing issues](https://github.com/jdi-testing/jdi-python/issues).

### Don't see your issue? Open one

Before you make your changes, check if an [issue already exists](https://github.com/jdi-testing/jdi-python/issues) for the change you want to make.

If you spot something new, [open an issue](https://github.com/jdi-testing/jdi-python/issues/new). We'll discuss the problem you want to fix.

When you're done making changes, open your PR and get it reviewed.

### Testing

In order to test the project, run pytest.

Please don't forget to set up the environment variable `TEST_PASSWORD`. For example:

For Windows `set TEST_PASSWORD=<password>`

```bash
pytest <path to the project>/tests --no-header --no-summary -q
```

You will be able to find log info in `<path to the project>/jdi.log`.