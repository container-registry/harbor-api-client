# ScheduleObj

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The schedule type. The valid values are &#39;Hourly&#39;, &#39;Daily&#39;, &#39;Weekly&#39;, &#39;Custom&#39;, &#39;Manual&#39; and &#39;None&#39;. &#39;Manual&#39; means to trigger it right away and &#39;None&#39; means to cancel the schedule.  | [optional] 
**cron** | **str** | A cron expression, a time-based job scheduler. | [optional] 
**next_scheduled_time** | **datetime** | The next time to schedule to run the job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


