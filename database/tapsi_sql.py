import mysql.connector as sql
from database import ICE
from random import randint
import datetime


class TapsilogSql:
    def __init__(self):
        self.eyes = ICE.ICE()
        self.cnt = sql.MySQLConnection(user='root', password='potatolifeform1', host='127.0.0.1', database='tapsilog')
        self.cursor = self.cnt.cursor()

    # Tapsilog Homelogs code
    def tapsilog_hlog_idgen(self):
        range_start = 10 ** (10 - 1)
        range_end = (10 ** 10) - 1
        return randint(range_start, range_end)

    # generates the id for visitors
    def visitor_id_generator(self):
        range_start = 10 ** (4 - 1)
        range_end = (10 ** 4) - 1
        return randint(range_start, range_end)

    # generates the id for the homeowners randomly, accompanied by the block and lot of the homeowner
    def hm_id_generator(self):
        range_start = 10 ** (3 - 1)
        range_end = (10 ** 3) - 1
        return randint(range_start, range_end)

    # Generates admin id for easy identification
    def admin_id_generator(self):
        range_start = 10 ** (5 - 1)
        range_end = (10 ** 5) - 1
        return randint(range_start, range_end)

    # Provide reference codes to the ones that registered a new account (homeowner and visitor)
    def admin_regcode_generator(self):
        range_start = 10 ** (8 - 1)
        range_end = (10 ** 8) - 1
        return randint(range_start, range_end)

    """ADMIN CRUD"""
    def add_admin(self, name, username, email, pwrd):
        try:
            id = self.admin_id_generator()
            encoded_id = self.eyes.encode(id)
            encoded_name = self.eyes.encode(name)
            encoded_username = self.eyes.encode(username)
            encoded_email = self.eyes.encode(email)
            encoded_pwrd = self.eyes.encode(pwrd)
            query = (
                f"INSERT INTO admin VALUES ('{encoded_id}', '{encoded_name}', '{encoded_username}', '{encoded_email}', '{encoded_pwrd}')")
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            print("Theres an error uncured ")

    def show_admin(self):
        try:
            self.results = []
            query = "SELECT * FROM admin"
            self.cursor.execute(query)
            for (a, b, c, d, e) in self.cursor:
                self.results.append([a, b, c, d, e])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)

            else:
                return self.results
        except:
            return "Theres an error uncured "


    def search_id(self, id):
        try:
            encoded = self.eyes.encode(id)
            self.results = []
            query = f"SELECT * FROM admin WHERE admin_id = '{encoded}'"
            self.cursor.execute(query)
            for (a, b, c, d, e) in self.cursor:
                self.results.append(a)
                self.results.append(b)
                self.results.append(c)
                self.results.append(d)
                self.results.append(e)
            for i, j in enumerate(self.results):
                self.results[i] = self.eyes.decode(j)
            return self.results
        except:
            return "Theres an error uncured "

    def update_admin(self, id, name, username, email, pwrd):
        try:
            encoded_id = self.eyes.encode(id)
            encoded_name = self.eyes.encode(name)
            encoded_username = self.eyes.encode(username)
            encoded_email = self.eyes.encode(email)
            encoded_pwrd = self.eyes.encode(pwrd)
            query = f"UPDATE admin SET admin_name='{encoded_name}', admin_uname='{encoded_username}', admin_email='{encoded_email}', admin_pass='{encoded_pwrd}' WHERE admin_id='{encoded_id}' "
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            print("Theres an error uncured ")

    def delete_admin(self, id):
        try:
            encoded_id = self.eyes.encode(id)
            query = f"DELETE FROM admin WHERE admin_id ='{encoded_id}'"
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    """LOG IN CRU (DELETE is not included since record cant be modified)"""
    def add_admin_log_in(self, id):
        try:
            encoded_id = self.eyes.encode(id)
            date = datetime.datetime.now()
            date_of_shift = date.strftime('%m-%d-%Y')
            time_login = date.strftime('%I:%M %p ')
            encoded_date_of_shift = self.eyes.encode(date_of_shift)
            encoded_time_login = self.eyes.encode(time_login)
            query = (f"INSERT INTO admin_logs VALUES ('{encoded_id}', '{encoded_time_login}', 'NaN', '{encoded_date_of_shift}')")
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    def add_admin_logout(self, id):
        try:
            encoded_id = self.eyes.encode(id)
            date = datetime.datetime.now()
            date_of_shift = date.strftime('%m-%d-%Y')
            encoded_date_of_shift = self.eyes.encode(date_of_shift)
            time_logout = date.strftime('%I:%M %p ')
            encoded_time_logout = self.eyes.encode(time_logout)
            query = f"UPDATE admin_logs SET admin_tout='{encoded_time_logout}' WHERE admin_id='{encoded_id}' and dateOfShift='{encoded_date_of_shift}' "
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    def show_admin_logs(self):
        try:
            self.results = []
            query = "SELECT * FROM admin_logs;"
            self.cursor.execute(query)
            for (a, b, c, d) in self.cursor:
                self.results.append([a, b, c, d])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)
            else:
                return self.results
        except:
            return "Theres an error uncured"

    """ADMIN REG CR (UPDATE a& DELETE not included since records like this doesn't need to modified"""
    def add_admin_reg(self, admin_id):
        try:
            encoded_id = self.eyes.encode(admin_id)
            reg_code = self.admin_regcode_generator()
            encoded_rcode = self.eyes.encode(reg_code)
            date = datetime.datetime.now().strftime('%m-%d-%Y')
            encoded_date = self.eyes.encode(date)

            query = (f"INSERT INTO admin_reg VALUES ('{encoded_id}', '{encoded_rcode}', '{encoded_date}')")
            self.cursor.execute(query)
            self.cnt.commit()
            return reg_code
        except:
            pass

    def show_admin_reg(self):
        try:
            self.results = []
            query = "SELECT * FROM admin_reg"
            self.cursor.execute(query)
            for (a, b, c) in self.cursor:
                self.results.append([a, b, c])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)
            else:
                return self.results
        except:
            return "Theres an error uncured"

    """HOMEOWNER CRUD"""
    def add_homeowner(self, fname, lname, blk, lot, cellnum, user, password, regcode):
        try:
            id = str(blk) + str(lot) + "-" + str(self.hm_id_generator())
            encoded_id = self.eyes.encode(id)
            encoded_fname = self.eyes.encode(fname)
            encoded_lname = self.eyes.encode(lname)
            encoded_blk = self.eyes.encode(blk)
            encoded_lot = self.eyes.encode(lot)
            encoded_cellnum = self.eyes.encode(cellnum)
            encoded_user = self.eyes.encode(user)
            encoded_password = self.eyes.encode(password)
            encoded_regcode = self.eyes.encode(regcode)
            query = (
                f"INSERT INTO homeowner VALUES ('{encoded_id}', '{encoded_fname}', '{encoded_lname}','{encoded_blk}','{encoded_lot}','{encoded_cellnum}','{encoded_user}','{encoded_password}','{encoded_regcode}')")
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    def show_homeowners(self):
        try:
            self.results = []
            query = "SELECT * FROM homeowner"
            self.cursor.execute(query)
            for (a, b, c, d, e, f, g, h, i) in self.cursor:
                self.results.append([a, b, c, d, e, f, g, h, i])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)

            else:
                return self.results
        except:
           return "Theres an error uncured "

    def show_homeowners_wICE(self):
        try:
            self.results = []
            query = "SELECT * FROM homeowner"
            self.cursor.execute(query)
            for (a, b, c, d, e, f, g, h, i) in self.cursor:
                self.results.append([a, b, c, d, e, f, g, h, i])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = j

            else:
                return self.results
        except:
           return "Theres an error uncured "

    def update_homeowners(self, id, fname, lname, blk, lot, cellnum, user, password):
        try:
            encoded_id = self.eyes.encode(id)
            encoded_fname = self.eyes.encode(fname)
            encoded_lname = self.eyes.encode(lname)
            encoded_blk = self.eyes.encode(blk)
            encoded_lot = self.eyes.encode(lot)
            encoded_cellnum = self.eyes.encode(cellnum)
            encoded_username = self.eyes.encode(user)
            encoded_pwrd = self.eyes.encode(password)
            query = f"UPDATE homeowner SET ho_fname='{encoded_fname}', ho_lastname='{encoded_lname}', ho_blk='{encoded_blk}', ho_lot='{encoded_lot}' , ho_cellnum='{encoded_cellnum}', ho_user='{encoded_username}', ho_pass='{encoded_pwrd}' WHERE ho_id='{encoded_id}')"
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            print("Theres an error uncured ")

    def delete_homeowner(self, id):
        try:
            encoded_id = self.eyes.encode(id)
            query = f"DELETE FROM homeowner WHERE ho_id ='{encoded_id}'"
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    """VISITOR CRUD"""
    def add_visitor_by_admin(self, affliation, fname, lname, celnum, email, reason, reg_code):
        try:
            id = self.visitor_id_generator()
            encoded_id = self.eyes.encode(id)
            encoded_affliation = self.eyes.encode(affliation)
            encoded_fname = self.eyes.encode(fname)
            encoded_lname = self.eyes.encode(lname)
            encoded_celnum = self.eyes.encode(celnum)
            encoded_email = self.eyes.encode((email))
            encoded_reason = self.eyes.encode(reason)
            encoded_regcode = self.eyes.encode(reg_code)
            query = f"INSERT INTO visitor (ho_id, vt_id, vt_fname, vt_lname, vt_celnum, vt_reason, vs_email, reg_code) VALUES ('{encoded_affliation}','{encoded_id}','{encoded_fname}', '{encoded_lname}', '{encoded_celnum}','{encoded_email}','{encoded_reason}', '{encoded_regcode}')"
            self.cursor.execute(query)
            self.cnt.commit()
        except:
           pass

    def show_visitor(self):
        try:
            self.results = []
            query = "SELECT * FROM visitor"
            self.cursor.execute(query)
            for (a, b, c, d, e, f, g, h,i) in self.cursor:
                self.results.append([a, b, c, d, e, f, g, h,i])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)

            else:
                 return self.results
        except:
           return "Theres an error uncured "

    def add_homeowner_login(self, id, array):
        try:
            encoded_id = self.eyes.encode(id)
            encoded_hid = self.eyes.encode(array[0])
            encoded_hlogs = self.eyes.encode(self.tapsilog_hlog_idgen())
            date = datetime.datetime.now()
            date_of_entry = date.strftime('%m-%d-%Y')
            time_login = date.strftime('%I:%M %p')
            if array[2] == date_of_entry:
                encoded_date_of_entry = self.eyes.encode(date_of_entry)
                encoded_time_login = self.eyes.encode(time_login)
                query = (f"INSERT INTO homeowner_logs VALUES ('{encoded_id}', '{encoded_hid}', '{encoded_date_of_entry}','{encoded_time_login}','NaN','{encoded_hlogs}')")
                self.cursor.execute(query)
                self.cnt.commit()
                return True
            else:
                return False
        except:
            pass

    def add_homeowner_logout(self, th_code):
        try:
            date = datetime.datetime.now()
            date_of_entry = date.strftime('%m-%d-%Y')
            time_logout = date.strftime('%I:%M %p')
            encoded_logout = self.eyes.encode(time_logout)
            encoded_th_code = self.eyes.encode(th_code)
            query = f"UPDATE homeowner_logs SET ho_exit='{encoded_logout}' WHERE th_code = '{encoded_th_code}' AND ho_exit = 'NaN'"
            self.cursor.execute(query)
            self.cnt.commit()
        except:
            pass

    def show_homeowner_logs(self):
        try:
            self.results = []
            query = "SELECT * FROM homeowner_logs"
            self.cursor.execute(query)
            for (a, b, c, d, e, f) in self.cursor:
                self.results.append([a, b, c, d, e, f])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)

            else:
                 return self.results
        except:
           return "Theres an error uncured "

    def show_home_ids(self):
        self.home_ids = []
        for i in self.show_homeowner_logs():
            self.home_ids.append(i[1])
        return self.home_ids

    def is_exit_nan(self, hid):
            self.results = []
            encoded_hid = self.eyes.encode(hid)
            date = datetime.datetime.now()
            date_of_entry = date.strftime('%m-%d-%Y')
            encoded_date_of_entry = self.eyes.encode(date_of_entry)
            query = f"SELECT * FROM homeowner_logs WHERE ho_id='{encoded_hid}' AND ho_exit = 'NaN' AND ho_date = '{encoded_date_of_entry}'"
            self.cursor.execute(query)
            for (a, b, c, d, e, f) in self.cursor:
                self.results.append([a, b, c, d, e, f])
            for index, array in enumerate(self.results):
                for i, j in enumerate(array):
                    self.results[index][i] = self.eyes.decode(j)

            if self.results:
                return self.results[0][5]
            if self.results is None:
                return False





    def close_connection(self):
        self.cursor.close()
        self.cnt.close()

#sel = TapsilogSql()
#print(sel.show_homeowner_logs()
#print(sel.is_exit_nan('11-221'))

