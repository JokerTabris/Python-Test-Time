import os
import datetime
import subprocess

def print_progress_bar(iteration, total, bar_length=30):
    progress = min(1.0, 1 - iteration / total)
    arrow = "=" * int(round(progress * bar_length))
    spaces = " " * (bar_length - len(arrow))
    print("\r[{0}] {1}%".format(arrow + spaces, int(progress * 100)), end="")

def main():
    title = "　　学年末試験　４日目　"
    year = 2024
    month = 3
    day = 10
    exam = 50
    rest = 15
    pre_start1 = "0830"
    start1 = "0900"
    period1 = "家庭総合"
    period2 = "数学A"
    period3 = ""

    pre_start_hh1 = int(pre_start1[0:2])
    pre_start_mm1 = int(pre_start1[2:4])
    time_pre_start1 = datetime.datetime(year, month, day, pre_start_hh1, pre_start_mm1)

    start_hh1 = int(start1[0:2])
    start_mm1 = int(start1[2:4])
    time_start1 = datetime.datetime(year, month, day, start_hh1, start_mm1)
    if start_hh1 < 10:
        str_start_hh1 = "0" + str(start_hh1)
    else:
        str_start_hh1 = str(start_hh1)
    if start_mm1 < 10:
        str_start_mm1 = "0" + str(start_mm1)
    else:
        str_start_mm1 = str(start_mm1)

    if int(start1[2:4]) < 60 - exam:
        end1 = start1[0:2] + str(int(start1[2:4]) + exam)
    else:
        if exam - (60 - int(start1[2:4])) < 10:
            end1 = str(int(start1[0:2]) + 1) + "0" + str(exam - (60 - int(start1[2:4])))
        else:
            end1 = str(int(start1[0:2]) + 1) + str(exam - (60 - int(start1[2:4])))
    end_hh1 = int(end1[0:2])
    end_mm1 = int(end1[2:4])
    time_end1 = datetime.datetime(year, month, day, end_hh1, end_mm1, 00, 00)
    if end_hh1 < 10:
        str_end_hh1 = "0" + str(end_hh1)
    else:
        str_end_hh1 = str(end_hh1)
    if end_mm1 < 10:
        str_end_mm1 = "0" + str(end_mm1)
    else:
        str_end_mm1 = str(end_mm1)

    if end_mm1 >= 5:
        anounce1 = str_end_hh1 + ":" + str(end_mm1 - 5) + ":00"
    else: 
        anounce1 = str(end_hh1 - 1) + ":" + str(60 - end_mm1 - 5) + ":00"

    if int(end1[2:4]) < 60 - rest:
        start2 = end1[0:2] + str(int(end1[2:4]) + rest)
    else:
        if rest - (60 - int(end1[2:4])) < 10:
            start2 = str(int(end1[0:2]) + 1) + "0" + str(rest - (60 - int(end1[2:4])))
        else:
            start2 = str(int(end1[0:2]) + 1) + str(rest - (60 - int(end1[2:4])))
    start_hh2 = int(start2[0:2])
    start_mm2 = int(start2[2:4])
    time_start2 = datetime.datetime(year, month, day, start_hh2, start_mm2, 00, 00)
    if start_hh2 < 10:
        str_start_hh2 = "0" + str(start_hh2)
    else:
        str_start_hh2 = str(start_hh2)
    if start_mm2 < 10:
        str_start_mm2 = "0" + str(start_mm2)
    else:
        str_start_mm2 = str(start_mm2)

    if int(start2[2:4]) < 60 - exam:
        end2 = start2[0:2] + str(int(start2[2:4]) + exam)
    else:
        if exam - (60 - int(start2[2:4])) < 10:
            end2 = str(int(start2[0:2]) + 1) + "0" + str(exam - (60 - int(start2[2:4])))
        else:
            end2 = str(int(start2[0:2]) + 1) + str(exam - (60 - int(start2[2:4])))
    end_hh2 = int(end2[0:2])
    end_mm2 = int(end2[2:4])
    time_end2 = datetime.datetime(year, month, day, end_hh2, end_mm2, 00, 00)
    if end_hh2 < 10:
        str_end_hh2 = "0" + str(end_hh2)
    else:
        str_end_hh2 = str(end_hh2)
    if end_mm2 < 10:
        str_end_mm2 = "0" + str(end_mm2)
    else:
        str_end_mm2 = str(end_mm2)

    if end_mm2 >= 5:
        anounce2 = str_end_hh2 + ":" + str(end_mm2 - 5) + ":00"
    else:
        anounce2 = str(end_hh2 - 1) + ":" + str(60 - end_mm2 - 5) + ":00"

    if int(end2[2:4]) < 60 - rest:
        start3 = end2[0:2] + str(int(end2[2:4]) + rest)
    else:
        if rest - (60 - int(end2[2:4])) < 10:
            start3 = str(int(end2[0:2]) + 1) + "0" + str(rest - (60 - int(end2[2:4])))
        else:
            start3 = str(int(end2[0:2]) + 1) + str(rest - (60 - int(end2[2:4])))
    start_hh3 = int(start3[0:2])
    start_mm3 = int(start3[2:4])
    time_start3 = datetime.datetime(year, month, day, start_hh3, start_mm3, 00, 00)
    if start_hh3 < 10:
        str_start_hh3 = "0" + str(start_hh3)
    else:
        str_start_hh3 = str(start_hh3)
    if start_mm3 < 10:
        str_start_mm3 = "0" + str(start_mm3)
    else:
        str_start_mm3 = str(start_mm3)

    if int(start3[2:4]) < 60 - exam:
        end3 = start3[0:2] + str(int(start3[2:4]) + exam)
    else:
        if exam - (60 - int(start3[2:4])) < 10:
            end3 = str(int(start3[0:2]) + 1) + "0" + str(exam - (60 - int(start3[2:4])))
        else:
            end3 = str(int(start3[0:2]) + 1) + str(exam - (60 - int(start3[2:4])))
    end_hh3 = int(end3[0:2])
    end_mm3 = int(end3[2:4])
    time_end3 = datetime.datetime(year, month, day, end_hh3, end_mm3, 00, 00)
    if end_hh3 < 10:
        str_end_hh3 = "0" + str(end_hh3)
    else:
        str_end_hh3 = str(end_hh3)
    if end_mm3 < 10:
        str_end_mm3 = "0" + str(end_mm3)
    else:
        str_end_mm3 = str(end_mm3)

    if end_mm3 >= 5:
        anounce3 = str_end_hh3 + ":" + str(end_mm3 - 5) + ":00"
    else: 
        anounce3 = str(end_hh3 - 1) + ":" + str(60 - end_mm3 - 5) + ":00"
    date_old = ""
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    while(1):
        dt = datetime.datetime.now()
        date = dt.strftime("%Y-%m-%d %H:%M:%S")
        format_date = dt.strftime("%H:%M:%S")
        if date != date_old:
            os.system("clear")
            if date >= time_start3.strftime("%Y-%m-%d %H:%M:%S"):
                if count6 == 1:
                    count6 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("  " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("  " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("▶ " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time6 = max(0, (time_end3 - dt).total_seconds())
                print("\033[39m" + "\n　　試験終了まで残り:", datetime.timedelta(seconds=int(remaining_time6)))
                print_progress_bar((time_end3 - dt).total_seconds(), (time_end3 - time_start3).total_seconds())
                if format_date == anounce3:
                    subprocess.run(["say", "あと５分です"])
            elif date >= time_end2.strftime("%Y-%m-%d %H:%M:%S"):
                if count5 == 1:
                    count5 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("  " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("  " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("▷ " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time5 = max(0, (time_start3 - dt).total_seconds())
                print("\033[39m" + "\n　　次の試験まで残り:", datetime.timedelta(seconds=int(remaining_time5)))
                print_progress_bar((time_start3 - dt).total_seconds(), (time_start3 - time_end2).total_seconds())
            elif date >= time_start2.strftime("%Y-%m-%d %H:%M:%S"):
                if count4 == 1:
                    count4 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("  " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("▶ " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("  " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time4 = max(0, (time_end2 - dt).total_seconds())
                print("\033[39m" + "\n　　試験終了まで残り:", datetime.timedelta(seconds=int(remaining_time4)))
                print_progress_bar((time_end2 - dt).total_seconds(), (time_end2 - time_start2).total_seconds())
                if format_date == anounce2:
                    subprocess.run(["say", "あと５分です"])
            elif date >= time_end1.strftime("%Y-%m-%d %H:%M:%S"):
                if count3 == 1:
                    count3 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("  " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("▷ " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("  " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time3 = max(0, (time_start2 - dt).total_seconds())
                print("\033[39m" + "\n　　次の試験まで残り:", datetime.timedelta(seconds=int(remaining_time3)))
                print_progress_bar((time_start2 - dt).total_seconds(), (time_start2 - time_end1).total_seconds())
            elif date >= time_start1.strftime("%Y-%m-%d %H:%M:%S"):
                if count2 == 1:
                    count2 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("▶ " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("  " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("  " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time2 = max(0, (time_end1 - dt).total_seconds())
                print("\033[39m" + "\n　　試験終了まで残り:", datetime.timedelta(seconds=int(remaining_time2)))
                print_progress_bar((time_end1 - dt).total_seconds(), (time_end1 - time_start1).total_seconds())
                if format_date == anounce1:
                    subprocess.run(["say", "あと５分です"])
            elif date >= time_pre_start1.strftime("%Y-%m-%d %H:%M:%S"):
                if count1 == 1:
                    count1 -= 1
                print("\033[37m" + title + format_date + "\n")
                print("▷ " + str_start_hh1 + ":" + str_start_mm1 + "~" + str_end_hh1 + ":" + str_end_mm1 + "　" + period1)
                if period2 != "":
                    print("  " + str_start_hh2 + ":" + str_start_mm2 + "~" + str_end_hh2 + ":" + str_end_mm2 + "　" + period2)
                if period3 != "":
                    print("  " + str_start_hh3 + ":" + str_start_mm3 + "~" + str_end_hh3 + ":" + str_end_mm3 + "　" + period3)
                remaining_time1 = max(0, (time_start1 - dt).total_seconds())
                print("\033[39m" + "\n　　試験まで残り:", datetime.timedelta(seconds=int(remaining_time1)))
                print_progress_bar((time_start1 - dt).total_seconds(), (time_start1 - time_pre_start1).total_seconds())
        date_old = date

if __name__ == "__main__":
    main()
