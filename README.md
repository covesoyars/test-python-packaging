# I learn how to package python code with local libraries

1. I will have two packages that rely on a third package:

    package_a <- package_c
    package_b <- package_c

2. package_a and package_c will contain dependencies on the same library, `requests`

3. Source dirs for package_a and package_b will contain requirements.txt files including package_c as a dependency.

