
def generate():
   f = open("init_json.sql", "a")
   insert = "insert into relational_test.json_test (event_type, event_last_timestamp, event_json_message) VALUES "    
   insertn = ""
   for i in range(20000):
        json_msg = "(\"int_down\", \"2016-06-22 19:10:25-07\", " \
        + "{\"commonEventHeader\":{\"event_id\":1,\"event_type\":\"int_down\",\"event_key\":\"int_down_" \
        + str(i).rjust(7, '0') \
        + "\",\"event_state\":\"raise\",\"event_nets_ticket\":\"nets_" \
        + str(i).rjust(7, '0') \
        + """\",\"event_start\":\"2016-06-22 19:10:25-07\",\"event_last_change\": 
        \"2016-06-22 19:10:25-07\",\"event_end\":\"2016-06-22 19:10:25-07\",\"event_flap_count\"
        :1,\"ticket_event_flap_count\":2,\"event_details\":{\"event_text\":\"TL1TSM_Atlantic7342\",
        \"event_detail_key\":\"detail_int_down_""" \
        + str(i).rjust(7, '0') \
        + """\",\"event_last_timestamp\":\"2016-06-22 19:10:25-07\",\"event_enrichments\":
        \"TL1TSM_Atlantic7342\",\"event_action\":\"action1\",\"event_action_delay\":10,
        \"no_auto_close\":0,\"last_nets_event_history_id\":0,\"last_nets_status_check\"
        :0,\"ticket_event_state\":\"active\",\"parent_event_id\":1,\"event_ticket_suppression_cause\"
        :\"nothing\",\"last_nets_worklog_addition\":0,\"event_correlation_id\":1,
        \"event_correlation_worklog_updated\":0}},\"faultFields\":
        {\"fault_id\":1,\"fault_type\":\"int_down\"}}""" + "),"
        insertn = insertn + json_msg    
   insert = insert + insertn[:-1]  + ";"
   f.write(insert + "\n")
   f.close()


if __name__ == '__main__':
   generate()