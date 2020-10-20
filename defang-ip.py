class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        addr = ""
        for i in range(0, len(address)):
            if address[i] == ".":
                addr += "[.]"
            else:
                addr += address[i]
        return addr