class Report:
    def __init__(self, levels):
        self.levels = levels

    def __str__(self):
        ret = str(str(l) + " " for l in self.levels)
        return ret
    
    def is_valid_f(levels, max_step):
        index = -1
        for l1, l2 in zip(levels[:-1], levels[1:]):
            index += 1
            if l1 > l2 >= l1 - max_step:
                pass
            else:
                return False, index
        return True, index

    def is_valid_r(levels, max_step):
        index = -1
        for l1, l2 in zip(levels[:-1], levels[1:]):
            index += 1
            if l1 < l2 <= l1 + max_step:
                pass
            else:
                return False, index
        return True, index
    
    def is_valid(self, max_step=3):
        if self.validity is None:
            self.validity, _ =  Report.is_valid_r(self.levels, max_step) or Report.is_valid_f(self.levels, max_step)
        return self.validity

    
    def test_valid(test_list, max_step=3):
        for i in range(len(test_list) - 1):
            ret1, _ = Report.is_valid_r(test_list[:i] + test_list[i + 1:], max_step)
            ret2, _ = Report.is_valid_f(test_list[:i] + test_list[i + 1:], max_step)
            if ret1 or ret2:
                return True
        
        ret1, _ = Report.is_valid_r(test_list[:-1], max_step)
        ret2, _ = Report.is_valid_f(test_list[:-1], max_step)
        if ret1 or ret2:
            return True
        else:
            return False
        
        """
        ret, idx = Report.is_valid_r(test_list, max_step)
        tmp = test_list[:idx] + test_list[idx + 1:]
        if not ret: 
            ret, _ = Report.is_valid_r(test_list[:idx] + test_list[idx + 1:], max_step)
        if ret:
            return True
        
        ret, idx = Report.is_valid_f(test_list, max_step)
        tmp = test_list[:idx] + test_list[idx + 1:]
        if not ret: 
            ret, _ = Report.is_valid_f(test_list[:idx] + test_list[idx + 1:], max_step)
        return ret
        """

def main(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    reports = [Report(list(map(int, line.strip().split()))) for line in lines]
    # print(Report.test_valid([71, 73, 73, 76, 79, 82, 85], 3))
    # return
    valid_report_sum = 0
    for rep in reports:
        if Report.test_valid(rep.levels, 3):
            valid_report_sum += 1
        # print(f'Report, {rep.levels}, is {rep.is_valid(3)}')
    print(valid_report_sum)
    return valid_report_sum
    

    
if __name__ == "__main__":
    assert main("test_input.txt") == 4
    assert main("input.txt") > 399
    print(main("input.txt"))