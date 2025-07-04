import pytest
from filter import apply_filter
from aggregate import aggregate


rows = [
    {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
    {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
    {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
    {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
]


def test_filter_price_less_than_500():
    result = apply_filter(rows, 'price<500')
    assert len(result) == 2
    assert {r['name'] for r in result} == {'redmi note 12', 'poco x5 pro'}


def test_filter_brand_equals_apple():
    result = apply_filter(rows, 'brand=apple')
    assert len(result) == 1
    assert result[0]['name'] == 'iphone 15 pro'


def test_filter_rating_more_than_4_7():
    result = apply_filter(rows, 'rating>4.7')
    assert len(result) == 2
    assert {r['brand'] for r in result} == {'apple', 'samsung'}

def test_aggregate_price_avg():
    result = aggregate(rows, 'price=avg')
    assert result[0]['result'] == pytest.approx((999 + 1199 + 199 + 299) / 4, 0.01)


def test_aggregate_price_max():
    result = aggregate(rows, 'price=max')
    assert result[0]['result'] == 1199.0


def test_aggregate_rating_min():
    result = aggregate(rows, 'rating=min')
    assert result[0]['result'] == 4.4
