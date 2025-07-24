import pytest
import pkg_resources

VULNERABLE = {
    'log4j': '2.14.1',
}

def test_scan_dependencies():
    for pkg, vuln_version in VULNERABLE.items():
        try:
            version = pkg_resources.get_distribution(pkg).version
            assert version != vuln_version
        except pkg_resources.DistributionNotFound:
            pass
