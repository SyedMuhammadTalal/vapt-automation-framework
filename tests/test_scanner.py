from scanner.port_scanner import start_scan

def test_scan():
    result = start_scan()
    assert isinstance(result, list)
    print("Scanner test passed")

if __name__ == "__main__":
    test_scan()