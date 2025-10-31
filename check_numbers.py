def all_positive(numbers):
    """
    تفحص إذا كانت كل الأرقام موجبة.
    """
    for n in numbers:
        if n <= 0:
            return False
    return True


# تجربة
nums = [3, 7, -2, 5]
print("القائمة:", nums)
print("هل جميعها موجبة؟", all_positive(nums))
