 # Windows Server
It is a powerful platform used for managing infrastructure, hosting applications, and providing services like file sharing, Active Directory, DNS, DHCP, and more.

### Promoting This server to a domain controller


## View All AD Groups
 Command:

Get-ADGroup -Filter * | Select Name, DistinguishedName | Format-Table

Explanation:
This lists all Active Directory groups in the domain.

Get-ADGroup -Filter *: fetches every group.

Select: shows only the group's Name and DistinguishedName.

Format-Table: displays the output in a readable table format.
