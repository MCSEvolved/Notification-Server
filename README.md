# Notification Server
This service can be used to send push notifications to the mobile devices of the MCS players.
## Topics
Services can send notifications to specific topics, clients can subscribe to these topics and will receive a notification if one is send to one of the topics they subscribed to.  
These are all the current topics, they all have an explanation on when to use them. If you want to add a topic, add an issue with the goal of the topic and for what service it is.
### List of Topics

<details>
<summary>Minecraft Server Status</summary>

| **Topic Name** | **Description** |
| --- | --- | 
| `mc-server` | For sending Minecraft Server status updates, e.g. when the server turns on/off |

</details>

<details>
<summary>Power Management</summary>

| **Topic Name** | **Description** |
| --- | --- |
| `power-management_shortage` | For sending a notification when there is a power shortage in the system |
| `power-management_reactor-shut-off` | For sending a notification when the reactor turns off |

</details>

<details>
<summary>Service Status</summary>

| **Topic Name** | **Description** |
| --- | --- |
| `service-status_tracker` | For sending a notification when the **Tracker Service** stops unexpectedly |
| `service-status_storage` | For sending a notification when the **Storage Service** stops unexpectedly |
| `service-status_emerald-exchange` | For sending a notification when the **Emerald Exchange Service** stops unexpectedly |
| `service-status_reactor-manager` | For sending a notification when the **Reactor Manager Service** stops unexpectedly |

</details>

<details>
<summary>Tracker</summary>

| **Topic Name** | **Description** |
| --- | --- |
| `tracker_error` | For sending a notification when a turtle sends an error |
| `tracker_warning` | For sending a notification when a turtle sends a warning |
| `tracker_out-of-fuel` | For sending a notification when a turtle is out of fuel |

</details>

<details>
<summary>Miscellaneous</summary>

| **Topic Name** | **Description** |
| --- | --- |
| `user_weekly-report` | For sending the weekly server report |

</details>


## API Documentation

### Send Notification (For Services Only)

<details>
<summary>Show Documentation</summary>

| Name | Value |
| --- | --- |
| URL | `api.mcsynergy.nl/notifications/send` |
| Method | `POST` |
| URL Params | `topic: string` |
| Body | ` JSON `
| Headers | `Authorization` |
| Required Claim | `isService` |
| Success Response | Code: 200 <br> Content: `response` |
| Error Response | Code: 400 <br> Content: `Topic Does Not Exist` |
| Error Response | Code: 400 <br> Content: `JSON is invalid` |
| Error Response | Code: 401 <br> Content: `Not Authorized` |

Request Body Example:
``` json
{
    "title":"Test Notification",
    "body":"This is a test notification"
} 
```

</details>


<!-- 
---

### Register Device and Subscribed Topics (For Mobile Clients Only)

<details>
<summary>Show Documentation</summary>

| Name | Value |
| --- | --- |
| URL | `api.mcsynergy.nl/notifications/register-device` |
| Method | `POST` |
| Body | ` JSON `
| Headers | `Authorization` |
| Required Claim | `isPlayer` |
| Success Response | Code: 200 <br> Content: `Successfully Registered and Subscribed to: [SUBSCRIBED_TOPICS]` |
| Error Response | Code: 400 <br> Content: `JSON is invalid` |
| Error Response | Code: 401 <br> Content: `Not Authorized` |

Request Body Example:
``` json
{
    "topics":["/topics/mc-server", "/topics/service-status/tracker", "/topics/tracker/error"],
    "registrationToken":"abcdefghijklmnopqrstuvwxyz1234567890"
} 
```
`registrationToken`: token of the device.

</details -->