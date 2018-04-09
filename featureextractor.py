def featureextractor(link):
    arr = []
    domain = link.split('/')
    # having_IP_Address  { -1,1 }
    try:
        parts = domain[3].split('.')
        if (len(parts) == 4 and all(0 <= int(part) < 256 for part in parts))
            arr.append(-1)
    except ValueError:
        arr.append(1)  # one of the 'parts' not convertible to integer
    except (AttributeError, TypeError):
        arr.append(1)
