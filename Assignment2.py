def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title
      
    def from_template(cls, template):
        return cls(template)

    def __str__(self):
        return f"Report Title: {self.title}"
      
    def generate(self):
        return f"This is the report: {self.title}"


if __name__ == "__main__":
    report = Report.from_template("Annual Performance")
    print(str(report))
    print(report.generate())
