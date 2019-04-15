import DateTimeFormat = Intl.DateTimeFormat;

export interface TaskList {
    id: number;
    name: string;
}
export interface Task {
  id: number;
  name: string;
  status: string;
  created_at: DateTimeFormat;
  due_on: DateTimeFormat;
}
