
def generate():
   f = open("init_relational.sql", "a")
   insert_sql = """INSERT INTO relational_test.relational_test 
   (event_type,event_key,event_state,event_nets_ticket,
   event_start,event_last_change,event_end,event_flap_count,
   ticket_event_flap_count,event_details,event_last_timestamp,
   event_enrichments,event_action,event_action_delay,
   no_auto_close,last_nets_event_history_id,last_nets_status_check,
   ticket_event_state,parent_event_id,event_ticket_suppression_cause,
   last_nets_worklog_addition,event_correlation_id,event_correlation_worklog_updated) VALUES """
   insertn = ""
   for i in range(10000, 20000):
      insertn = insertn + "('int_down','int_down_" \
      + str(i).rjust(7, '0') \
      + "',NULL,NULL,'2016-06-22 19:10:25-07','2016-06-22 19:10:25-07','2016-06-22 19:10:25-07',0,0,NULL,'2016-06-22 19:10:25-07',NULL,'',0,0,0,0,'',0,'',0,0,0),"      
   insertn = insertn[:-1]   
   insert_sql = insert_sql + insertn + ';'
   f.write(insert_sql + "\n")
   f.close()


if __name__ == '__main__':
   generate()