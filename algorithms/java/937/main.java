class Solution {
    class Log{
        String id;
        String log;
        Log(String id, String log){
            this.id = id;
            this.log = log;
        }
    }
    public String[] reorderLogFiles(String[] logs) {
        if(logs == null || logs.length == 0){
            return logs;
        }
        String[] res = new String[logs.length];
        ArrayList<Log> letters = new ArrayList<Log>();
        ArrayList<String> digits = new ArrayList<String>();
        for(String log: logs){
            int idx = log.indexOf(' ');
            String id = log.substring(0, idx);
            String l = log.substring(idx + 1);
            if(l.charAt(0) >= '0' && l.charAt(0) <= '9'){
                digits.add(log);
            } else {
                letters.add(new Log(id, l));
            }
        }
        Comparator<Log> comparator = new Comparator<Log>(){
            @Override
            public int compare(Log first, Log second){
                int res = first.log.compareTo(second.log);
                if(res == 0){
                    res = first.id.compareTo(second.id);
                }
                return res;
            }
        };
        Collections.sort(letters, comparator);
        int i = 0;
        for(Log l: letters){
            res[i] = l.id + " " + l.log;
            i ++;
        }
        for(String s: digits){
            res[i] = s;
            i ++;
        }
        return res;
    }
}