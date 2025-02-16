from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_data: list[dict]):
    """Тестирование функции filter_by_state с параметром state по умолчанию"""
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"
    assert result[1]["state"] == "EXECUTED"


def test_filter_by_state_canceled(sample_data: list[dict]):
    """Тестирование функции filter_by_state с параметром state='CANCELED'"""
    result = filter_by_state(sample_data, state="CANCELED")
    assert len(result) == 2
    assert result[0]["state"] == "CANCELED"
    assert result[1]["state"] == "CANCELED"


def test_filter_by_state_empty(sample_data: list[dict]):
    """Тестирование функции filter_by_state при отсутствии элементов по заданному state"""
    result = filter_by_state(sample_data, state="PENDING")
    assert len(result) == 0


def test_sort_by_date_descending(sample_data: list[dict]):
    """Тестирование функции sort_by_date в порядке убывания"""
    result = sort_by_date(sample_data)
    assert result[0]["date"] > result[1]["date"]
    assert result[1]["date"] > result[2]["date"]
    assert result[2]["date"] > result[3]["date"]


def test_sort_by_date_ascending(sample_data: list[[dict]]):
    """Тестирование функции sort_by_date в порядке возрастания"""
    result = sort_by_date(sample_data, reverse=False)
    assert result[0]["date"] < result[1]["date"]
    assert result[1]["date"] < result[2]["date"]
    assert result[2]["date"] < result[3]["date"]


def test_sort_by_date_same_date(sample_data: list[dict]):
    """Тестирование функции sort_by_date с одинаковыми датами"""
    sample_data[1]["date"] = sample_data[0]["date"]
    result = sort_by_date(sample_data)
    assert result[0]["date"] == result[1]["date"]
    assert result[0]["date"] >= result[2]["date"]
    assert result[2]["date"] >= result[3]["date"]
